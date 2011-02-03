#! /bin/bash

PATH=$1

MSG="You need to specify the PATH to your project folder (e.g. ~/bhp056). Optionally add main application name, MYAPPNAME, (e.g. mochudi or mpepu, etc)."
USAGE="Usage: $0 PATH [MYAPPNAME]"


if [ -z $1 ] ; then
  echo $MSG
  echo $USAGE
  exit 1
fi

if [ $2 ] ; then
  echo "$2"
  cd $PATH/$2
  /usr/bin/svn commit -m ""
  /usr/bin/svn update
  /usr/bin/svn status
fi

echo "bhp_choices"
cd $PATH/bhp_choices
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_choices"
cd $PATH/bhp_choices
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_fields"
cd $PATH/bhp_fields
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_validators"
cd $PATH/bhp_validators
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_admin_models"
cd $PATH/bhp_admin_models
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_consent"
cd $PATH/bhp_consent
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_basic_models"
cd $PATH/bhp_basic_models
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_clinic_models"
cd $PATH/bhp_clinic_models
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_variables"
cd $PATH/bhp_variables
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_code_lists"
cd $PATH/bhp_code_lists 
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

echo "bhp_lab"
cd $PATH/bhp_lab
/usr/bin/svn commit -m ""
/usr/bin/svn update
/usr/bin/svn status

exit 0
