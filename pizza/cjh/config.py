#!/usr/bin/env python
"""
Config objects stores configuration information and methods to read/write the
./config.json file.
"""
import json, sys, traceback, time

from cjh import cli

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

try:
    from cjh.dialog_gui import DialogGui
    from cjh.tk_template import TkTemplate
    #import cjh.tk_template
    from cjh.wx_template import WxTemplate
except ImportError:
    pass

class Config(object):
    """
    This should be combined with Shellib
    """

    def __init__(self):
        """
        Get directory name of config file.
        """
        if cli.Cli().platform == 'android':
            self.basedir =\
        '/storage/sdcard0/com.hipipal.qpyplus/lib/python2.7/site-packages/cjh'
        else: self.basedir = 'cjh'
        self.sh_class = cli.Cli()
        try:
            self.read_config_file()
        except IOError:
            self.config_dict = {
                'editor': 'scite',
                'shell': 'bash',
                'terminal': 'terminator -e',
                'language': 'EN'
            }
            self.write_to_config_file(**self.config_dict)

    def read_config_file(self):
        """
        Find the config.json file and load the specified shell.
        """
        # Load json file and retrieve data.
        if sys.version_info.major == 2:
            self.config_dict = json.load(
                open('{}/config.json'.format(self.basedir), 'rb'))
        else: #i.e., if sys.version_info.major == 3:
            file_handler = open('{}/config.json'.format(self.basedir), 'rb')
            file_str = file_handler.read().decode('utf-8')
            self.config_dict = json.loads(file_str)

    def start_user_profile(self):
        """
        Launches specified shell.
        """
        self.read_config_file()
        shell = self.config_dict['shell']
        self.sh_class = self.launch_selected_shell(shell)
        return self.sh_class

    def get_lang_key(self):
        return self.config_dict['language']

    def write_to_config_file(self, **kwargs):
        """
        Writes preferences as JSON
        """
        self.config_dict.update(kwargs)
        with open('{}/config.json'.format(self.basedir), 'w') as outfile:
            json.dump(self.config_dict, outfile, indent=2)
            outfile.close()

    @staticmethod
    def launch_selected_shell(shl):
        """
        Select appropriate UI class from cjh.shell module
        Perhaps move this to some other class, or no class.
        """
        if shl in ['dialog', 'SL4A', 'zenity']:
            sh_class = DialogGui(shl)
        elif shl == 'Tk':
            try:
                sh_class = TkTemplate()
            except SystemExit:
                cli.ellipses("Display not found.  Defaulting to 'bash'")
                print('') #pylint: disable=C0325
                sh_class = cli.Cli()
                print(traceback.format_exc()) #pylint: disable=C0325
                time.sleep(4)
        elif shl == 'wx':
            try:
                sh_class = WxTemplate()
            except SystemExit:
                cli.ellipses("Display not found.  Defaulting to 'bash'")
                print('') #pylint: disable=C0325
                sh_class = cli.Cli()
                print(traceback.format_exc()) #pylint: disable=C0325
                time.sleep(4)
        else: sh_class = cli.Cli()
        return sh_class

