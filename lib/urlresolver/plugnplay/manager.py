'''
    urlresolver XBMC Addon
    Copyright (C) 2011 t0mm0
    based on plugnplay by https://github.com/daltonmatos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

'''
  The main plugin Manager class.
  Stores all implementors of all public interfaces
'''
class Manager(object):

    def __init__(self):
        self.iface_implementors = {}

    def binary_search(self, array, target):
        ''' compFunc is a bit weird, but works fine for what we need in the manager.
        It receives the array, the target and the index, just in case extra
        processing in the array is necessary
        '''
        lower = 0
        upper = len(array)
        index = lower + (upper - lower) // 2
        while lower < upper:  # use < instead of <=
            if array[index].priority == target.priority:
                if array[index].name > target.name:
                    if lower == index: break
                    lower = index
                elif array[index].name < target.name:
                    upper = index
                else:
                    return index
            elif array[index].priority > target.priority:
                if lower == index: break 
                lower = index
            elif array[index].priority < target.priority:
                upper = index
                if lower == upper:
                    return index + 1
            index = lower + (upper - lower) // 2
        return index



    def add_implementor(self, interface, implementor_instance):
        self.iface_implementors.setdefault(interface, [])
        index = self.binary_search(self.iface_implementors[interface], implementor_instance)
        self.iface_implementors[interface].insert(index, implementor_instance)
        # self.iface_implementors[interface].append(implementor_instance)

    def implementors(self, interface):
        return self.iface_implementors.get(interface, [])
