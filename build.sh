#!/bin/sh

rm -a ~/rpmbuild/BUILD
cp -a patch/ ~/rpmbuild/BUILD
rpmbuild -bb -v rpm/sailfish-weather-widget-patch.spec
