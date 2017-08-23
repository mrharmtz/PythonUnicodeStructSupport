# -*- coding: utf-8 -*-
import unicodedata


def uni_from_obj(uni_str):
    '''
    simpley tries to encode the object to unicode
    this method is called by default
    :param uni_str: the object to encode
    :return: unicode string of the object
    '''
    return unicode(uni_str)


def uni_from_tuple(uni_tup):
    '''
    encodes a tuple struct, each element in the tuple is sent for encoding as well
    :param uni_tup: the tuple to encode
    :return: tuple encoded to unicode
    '''
    if type(uni_tup) is not tuple:
        raise ValueError('wrong type passed to output_unicode_tuple()')
    result = u'('
    start_flag = False
    for entity in uni_tup:
        if start_flag:
            result += u', '
        result += uni_from_struct(entity)
        start_flag = True
    return result + u')'


def uni_from_dict(uni_dict):
    '''
    encodes a dictionary, each key and value are sent for encoding as well
    :param uni_dict: the dictionary to encode
    :return: dictionary encoded to unicode
    '''
    if type(uni_dict) is not dict:
        raise ValueError('wrong type passed to output_unicode_dict()')
    result = u'{'
    start_flag = False
    for key,entity in uni_dict.iteritems():
        if start_flag:
            result += u', '
        result += uni_from_struct(key)
        result += u': '
        result += uni_from_struct(entity)
        start_flag = True
    return result + u'}'


def uni_from_list(uni_list):
    '''
    encodes a list, each element is sent to encoding as well
    :param uni_list: the list to encode
    :return: list encoded to unicode
    '''
    if type(uni_list) is not list:
        raise ValueError('wrong type passed to output_unicode_list()')
    result = u'['
    start_flag = False
    for entity in uni_list:
        if start_flag:
            result += u', '
        result += uni_from_struct(entity)
        start_flag = True
    return result + u']'


def uni_from_struct(uni_data):
    '''
    the main function to encode a python struct
    :param uni_data: the struct to encode to unicode
    :return: struct encoded to unicode
    '''
    global DEFAULT_PARSE_TABLE
    return DEFAULT_PARSE_TABLE.get(type(uni_data), uni_from_obj)(uni_data)

# the main parsing dictionary, if you wish to add a new stuct to encode,
# add it to this dictionary as DEFAULT_PARSE_TABLE[<type of struct>] = <method for encoding>
# also possible to see an example in ExampleStructToUnicodeString.py
DEFAULT_PARSE_TABLE = {type([]): uni_from_list, type({}): uni_from_dict, type(()): uni_from_tuple }
