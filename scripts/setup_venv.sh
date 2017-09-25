export VENVSYS=$B2KTAUMUROOT/python/venv
if [ -d $VENVSYS ]; then
    source $VENVSYS/bin/activate
    
    echo "Configuring PYVENV     from $VENVSYS"
else
    echo
    echo "Creating    PYVENV     at $VENVSYS"
    echo
    virtualenv -p `which python` $VENVSYS
    source $VENVSYS/bin/activate
    
    REQ=$B2KTAUMUROOT/python/venv_requirements.txt
    if [ -f $REQ ]; then
	echo "Installing packages from $REQ"
	echo
	cat $REQ
	echo
	if [ -n "${TMPDIR+x}" ]; then
	    TMP=$TMPDIR
	    unset TMPDIR
	fi
	pip install -r $REQ
	if [ -n "${TMP+x}" ]; then
	    export TMPDIR=$TMP
	fi
	echo
	ls -l $VENVSYS/lib/python2.7/site-packages
	echo
    fi
fi

