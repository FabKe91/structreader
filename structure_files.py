''' Generic functions and constants are stored here
Some infos to re package:
        match with
                regular_expression = re.compile(r"regexppattern")
                regular_expression.match(str) -> match_obj or None
                grps = match_obj.group(index) returns group at index, input can also be list of indices, index 0 is entire match
                grps = match_obj.groups() returns tuple of all subgroups


'''
import re

XYZ_STRING_FORMAT = '{: >15}{: >20}{: >20.6f}{: >20.6f}{: >20.6f}'
XYZ_PATTERN = r"""
\s+
        (?P<atom>[\w,\d,\+]+)
\s+
        (?P<x>\d+.\d+)  (?# X)
\s+
        (?P<y>\d+.\d+)  (?# Y)
\s+
        (?P<z>\d+.\d+)  (?# Z)
"""
XYZ_PATTERN = ''.join(XYZ_PATTERN.split()) # Remove all whitespaces in above defined pattern
REGEX_XYZ   = re.compile(XYZ_PATTERN)



PDB_REC = 'ATOM'
#                    Record   Serial   atomname    resn    resid        x       y           z    Rest
PDB_STRING_FORMAT = '{: <4}  {: >5} {: >2}{: <2}{}{: >4}{}{: >4}{}   {: >8.3f}{: >8.3f}{: >8.3f}{}'#{: >6.2f}{: >6.2f}'
PDB_PATTERN = r"""
        ^
        ATOM              (?# Record Type)
\s+
        (?P<serial>\d+)             (?# Serial numbers  Grp 1)
\s*
        (?P<atm1>\w+?)(?P<atm2>[\d,\w,\']*)       (?# Atom names;     Grp 2+3)
\s+
        (?P<resn>[\w,\d]+)        (?# Residue name    Grp 4)
\s+
        (?P<resid>\d+)             (?# Resid           Grp 5)
\s+
        (?P<X>-?\d+\.\d+)      (?# X               Grp 6-8)
\s*
        (?P<Y>-?\d+\.\d+)      (?# Y)
\s*
        (?P<Z>-?\d+\.\d+)      (?# Z)
        (?P<remains>.*)              (?# Remainder)
            """
PDB_PATTERN = ''.join(PDB_PATTERN.split()) # Remove all whitespaces in above defined pattern
REGEX_PDB = re.compile(PDB_PATTERN)


#                     resid resnm atmnm atmnr   x        y         z         vx      vy        vz
GRO_STRING_FORMAT = '{: >5}{: <5}{: >5}{: >5}{: >8.3f}{: >8.3f}{: >8.3f}'#{: >8.4f}{: >8.4f}{: >8.4f} '
GRO_PATTERN = r"""
(?P<resid>[\s,\d]{5})           (?# Resid       Grp 1)
(?P<resn>[\s,\w]{5})           (?# Resname     Grp 2)
(?P<atm1>[\w,\s,\d,\']{5})           (?# Atom name   Grp 3)
(?P<atm2>[\s,\d]{5})           (?# Atom number Grp 4)
\s*
        (?P<X>-?\d+\.\d+)      (?# X               Grp 5-7)
\s*
        (?P<Y>-?\d+\.\d+)      (?# Y)
\s*
        (?P<Z>-?\d+\.\d+)      (?# Z)
\s*
        (?P<remains>.*)            (?# The rest velocities Grp 8)
"""
GRO_PATTERN = ''.join(GRO_PATTERN.split())
REGEXP_GRO = re.compile(GRO_PATTERN)
GRO_BOX_PATTERN = r'\s*(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)$'
REGEXP_BOX = re.compile(GRO_BOX_PATTERN)
