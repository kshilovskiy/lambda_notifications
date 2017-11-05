PATH_TO_FUNCTION=$1
TEMP_FOLDER="temp"
FUNCTION_ARCHIVE="function.zip"

if [ ! -d "$PATH_TO_FUNCTION" ]; then
  echo "No such folder '$PATH_TO_FUNCTION'"
  exit 1
fi



cd $PATH_TO_FUNCTION

if [ -d $TEMP_FOLDER ] ; then
    rm -r $TEMP_FOLDER
fi

mkdir "$TEMP_FOLDER"

if [ -f $FUNCTION_ARCHIVE ] ; then
    rm $FUNCTION_ARCHIVE
fi

# Required libraries for the function
pip install -r requirements.txt --target $TEMP_FOLDER

# Copy python scripts of the function
rsync -a --prune-empty-dirs --include '*.py' --exclude '/temp' . temp/

cd temp
zip -r ../$FUNCTION_ARCHIVE .
cd ..

rm -r $TEMP_FOLDER


echo "Function and resources compressed into $FUNCTION_ARCHIVE"
