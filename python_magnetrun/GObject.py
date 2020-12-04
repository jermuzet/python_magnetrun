#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""Magnet component Object"""

import json

class GObject:
    """
    name
    cadref
    geometry: yaml file
    material: dict of physical properties (sigma0, rpe) only 
    cf json mat in feelp to complete ??
    category: Helix, Ring, Current Lead, Bitter
    status: Dead/Alive
    """

    def __init__(self, name: str, cadref: str, geofile: str, material: dict, category: str, status: str):
        """default constructor"""
        self.name = name
        self.cadref = cadref
        self.geofile = geofile
        self.material = material
        self.category = category
        self.status = status

    def __repr__(self):
        """
        representation of object
        """
        return "%s(name=%r, cadref=%r, geofile=%r, material=%r, category=%r, status=%r)" % \
            (self.__class__.__name__,
             self.name,
             self.cadref,
             self.geofile,
             self.material,
             self.category,
             self.status
            )

    def setCadref(self, cadref):
        """set cadref"""
        self.cadref = cadref

    def getCadref(self):
        """get cadref"""
        return self.cadref

    def setStatus(self, status):
        """set status"""
        self.status = status

    def getStatus(self):
        """get status"""
        return self.status

    def setCategory(self, category):
        """set category"""
        self.category = category

    def getCategory(self):
        """get category"""
        return self.category

    def getMaterial(self):
        """get Material"""
        return self.material

    def getMaterialProperty(self, mproperty):
        """get Material Property"""
        return self.material[mproperty]

    def setMaterial(self, material):
        """set Material"""
        self.material = material

    def setMaterialProperty(self, mproperty, mval):
        """set Material Property"""
        self.material[mproperty] = mval
    


    def to_json(self):
        """
        convert to json
        """
        import deserialize
        return json.dumps(self, default=deserialize.serialize_instance, sort_keys=True, indent=4)