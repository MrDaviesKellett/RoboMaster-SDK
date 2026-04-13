basepath=$(cd `dirname $0`; pwd)
cd $basepath
cd ..
rm -rf build dist output robomaster_media_decoder.egg-info

PYTHON_TAGS=${PYTHON_TAGS:-"cp314-cp314 cp314-cp314t"}

for tag in $PYTHON_TAGS; do
    rm -rf build dist output robomaster_media_decoder.egg-info
    interpreter="/opt/python/${tag}/bin/python"
    auditwheel_bin="/opt/python/${tag}/bin/auditwheel"
    if [ ! -x "$interpreter" ]; then
        echo "skip missing interpreter: $interpreter"
        continue
    fi

    "$interpreter" setup.py build
    "$interpreter" setup.py bdist_wheel
    wheel_name=$(ls ./dist | grep "$tag" | head -n 1)
    if [ -n "$wheel_name" ] && [ -x "$auditwheel_bin" ]; then
        "$auditwheel_bin" repair "./dist/$wheel_name"
    fi
done
