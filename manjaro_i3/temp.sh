#!/bin/bash


userdata_dir="/userdata/171680367"

directory_store=("/config" "/compatibilitytools.d" "$userdata_dir/config" "$userdata_dir/7/remote")
# echo "directory_store = "${directory_store[@]}

for item in ${directory_store[@]}
do
echo $item
done
