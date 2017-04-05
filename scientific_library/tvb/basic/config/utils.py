# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2017, Baycrest Centre for Geriatric Care ("Baycrest") and others
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#

"""
Helper tools, for the configuration area.

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa@codemart.ro>
.. moduleauthor:: marmaduke <duke@eml.cc>

"""


class EnhancedDictionary(dict):
    """
    A dictionary like class that provides easy access to configuration values.
    """

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value



class LibraryImportError(ImportError):
    """
    This is just a flag telling us at "reload" that a module was rejected due to our custom exception
    """



class LibraryModulesFinder():
    """
    In case users run TVB in 'library' profile access should be restricted to some parts of tvb,
    to avoid errors from those parts (which are not excepted to run with library settings).
    """

    restricted_modules = ['tvb.interfaces',
                          'tvb.datatype_removers',
                          'tvb.core',
                          'tvb.config',
                          'tvb.adapters']


    def find_module(self, fullname, path=None):

        for restricted in self.restricted_modules:
            if fullname.startswith(restricted):
                return self


    def load_module(self, module_name):
        info_message = str("You are trying to import the module `%s` in library mode."
                           "The library profile is a lightweight version of TVB and you "
                           "only have access to the simulator, analyzers and datatypes packages."
                           "If you want to use the entire TVB Framework start it either in command "
                           "or web interface profile." % module_name)
        raise LibraryImportError(info_message)

