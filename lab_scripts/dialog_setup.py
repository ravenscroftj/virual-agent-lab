# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import DialogV1
import variables

dialog = DialogV1(
    username=variables.DIALOG_USERNAME,
    password=variables.DIALOG_PASSWORD)

# print(json.dumps(dialog.get_dialogs(), indent=2))

# CREATE A DIALOG
# Make sure you rename the dialog as this must be globally unique. Try apending your initials
with open(join(dirname(__file__), '../dialog_config/gem_dialog.xml')) as dialog_file:
    print(json.dumps(dialog.create_dialog(
        dialog_file=dialog_file, name='gem-dialog-oc3'), indent=2))
    print("*****Remember to copy the dialog_id to the bottom of the variables file*****")