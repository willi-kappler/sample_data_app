#!/usr/bin/env bash

# Remove old Python source code:
rm *.py *.pyc

# Copy all source code files to current folder (buildozer):
cp ../src/sample_data_app/main.py .
cp ../src/sample_data_app/sd_choose_file.py .
cp ../src/sample_data_app/sd_confirm_delete.py .
cp ../src/sample_data_app/sd_edit_data.py .
cp ../src/sample_data_app/sd_list_view.py .
cp ../src/sample_data_app/sd_main_menu.py .
cp ../src/sample_data_app/sd_scan_qr.py .
cp ../src/sample_data_app/sd_show_error.py .

# Generate Android APK file using apptainer:
apptainer run buildozer.sif -v android debug
