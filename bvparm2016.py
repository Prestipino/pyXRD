## ACCUMULATED TABLE OF BOND VALENCE PARAMETERS
#
#data_BOND_VALENCE_PARAMETERS_2016-10-28
#
## BVPARM.CIF
#_audit_conform_dict_name        cif_core.dic
#_audit_conform_dict_version     2.2
#
#
##***************************************************************
## COPYRIGHT NOTICE
## This table may be used and distributed without fee for
## non-profit purposes providing 
## 1) that this copyright notice is included and 
## 2) no fee is charged for the table and 
## 3) details of any changes made in this list by anyone other than
## the copyright owner are suitably noted in the _audit_update record
## Please consult the copyright owner regarding any other uses.
##
## The copyright is owned by I. David Brown, Brockhouse Institute for
## Materials Research, McMaster University, Hamilton, Ontario Canada.
## idbrown@mcmaster.ca
##
##*****************************DISCLAIMER************************
##
## The values reported here are taken from the literature and
## other sources and the author does not warrant their correctness
## nor accept any responsibility for errors.  Users are advised to
## consult the primary sources. 
##
##***************************************************************
##
## The latest version of this file is available at:
##
## http://www.iucr.org/resources/data/datasets/bond-valence-parameters
##
## The parameters given in the main table are the values of Ro and
## B used in the equation:
##
##     bond valence = exp((Ro-R)/B)
##
## where R is the bond length.  All values are in Angstrom units. 
## Where significantly different values have been reported in the
## literature, they are listed in decreasing order of reliability.
##
##     Bond valence parameters for atoms whose oxidation state is
## given as 9 do not have an oxidation state
## specified in the original paper.  They may apply to a
## particular, but unspecified, oxidation state or they may be
## intended to apply to all oxidation states.
##
##     The ammonium ion is listed under the symbol NH.
##
##     The list below is formatted and is designed to be read
## either as a crystallographic information file (CIF) or as a
## fixed format file once the text and associate data items 
## have been stripped off. A question mark in the final column is
## a place holder that indicates that there is no comment.
#####################################################################3
#
#_audit_creation_date         2001-02-21
_audit_update_record='''         
;2001-03-13 Ref m deleted.
 2001-06-01
 2001-06-21 new ref c and d added.
 2002-03-22 new ref q added
 2003-02-17 refs m, z and aa added
 2003-02-19 corrected CIF errors
 2004-08-12 correction of errors
 2006-05-02 refs ag to ai added
 2007-01-20 refs ag to am added
 2009-08-20 refs an to be added
 2011-06-01 refs bf to bh added
 2013-09-11 refs bi to bk added
         correction of syntax errors, 
         correcting Mo to Mn for parameters from ref. ap
 2016-10-28 refs bl to bs added
 '''
#;
#_audit_author_name           'I. David Brown'
#_audit_author_address
#;                            Brockhouse Institute for Materials Research
#                             McMaster University
#                             Hamilton, Ontario, Canada L8S 4M1
#;
#_audit_contact_author_name   'I. David Brown'
#_audit_contact_author_email  idbrown@mcmaster.ca  
#
#loop_
#     
#     _valence_ref_reference
_valence_ref_id = {
 'a' : 'Brown and Altermatt, (1985), Acta Cryst. B41, 244-247 (empirical)',
 'b' : 'Brese and O\'Keeffe, (1991), Acta Cryst. B47, 192-197 (extrapolated)',
 'c' : 'Adams, 2001, Acta Cryst. B57, 278-287 (includes second neighbours)',
 'd' : 'Hu et al. (1995) Inorg. Chim. Acta, 232, 161-165. ',
 'e' : 'I.D.Brown Private communication',
 'f' : 'Brown et al. (1984) Inorg. Chem. 23, 4506-4508',
 'g' : 'Palenik (1997) Inorg. Chem. 36 4888-4890',
 'h' : 'Kanowitz and Palenik (1998) Inorg. Chem. 37 2086-2088',
 'i' : 'Wood and Palenik (1998) Inorg. Chem. 37 4149-4151',
 'j' : 'Liu and Thorp (1993) Inorg. Chem. 32 4102-4105',
 'k' : 'Palenik (1997) Inorg. Chem. 36 3394-3397',
 'l' : 'Shields, Raithby, Allen and Motherwell (2000) Acta Cryst.B56, 455-465' ,
 'm' : 'Chen, Zhou and Hu (2002) Chinese Sci. Bul. 47, 978-980.',
 'n' : 'Kihlbourg (1963) Ark. Kemi 21 471-495; Schroeder 1975 Acta Cryst. B31, 2294',
 'o' : 'Allmann (1975) Monatshefte Chem. 106, 779',
 'p' : 'Zachariasen (1978) J.Less Common Metals 62, 1',
 'q' : 'Krivovichev and Brown (2001) Z. Krist. 216, 245',
 'r' : 'Burns, Ewing and Hawthorne (1997) Can. Miner. 35,1551-1570',
 's' : 'Garcia-Rodriguez, et al. (2000) Acta Cryst. B56, 565-569',
 't' : 'Mahapatra et al. (1996) J. Amer.Chem. Soc. 118, 11555',
 'u' : 'Wood and Palenik (1999) Inorg. Chem. 38, 1031-1034',
 'v' : 'Wood and Palenik (1999) Inorg. Chem. 38, 3926-3930',
 'w' : 'Wood, Abboud, Palenik and Palenik (2000) Inorg. Chem. 39, 2065-2068',
 'x' : 'Tytko, Mehnike and Kurad (1999) Structure and Bonding 93, 1-66',
 'y' : 'Gruendemann, et al.(1999) J. Phys. Chem. A 103, 4752-4754',
 'z' : 'Zocchi (2000) Solid State Sci. 2 383-387',
 'aa' : 'Jensen, Palenik and Tiekiak (2001) Polyhedron 20, 2137',
 'ab' : 'Roulhac and Palenik (2003) Inorg. Chem. 42, 118-121',
 'ac' : 'Holsa et al.(2002) J.Solid State Chem 165, 48-55',
 'ae' : 'Trzesowska, Kruszynski & Bartezak (2004) Acta Cryst. B60, 174-178',
 'af' : 'Locock & Burns (2004) Z.Krist. 219, 259-266',
 'ag' : 'Hu & Zhou (2004) Z. Krist. 219 614-620',
 'ah' : 'Trzesowska, Kruszynski & Bartczak (2005) Acta Cryst. B61 429-434',
 'ai' : 'Palenik (2003) Inorg. Chem. 42, 2725-2728',
 'aj' : 'Hong, Zhou & Hu (2004) Acta Chimica Sinica 62, 1733-1737',
 'ak' : 'Sidey (2006) Acta Cryst. B62, 949-951',
 'al' : 'Trzeowska, Kruszynski & Bartczak (2006) Acta Cryst. B62, 745-753',
 'am' : 'Malcherek & Schlueter (2007) Acta Cryst. B63, 157-160',
 'an' : 'Palenik, Abboud & Palenik (2005) Inorg. Chim. Acta 358, 1034',
 'ao' : 'Palenik (2006) Can. J. Chem. 84, 99',
 'ap' : 'Urusov (2006) Dokl. Phys. Chem. 408, 152',
 'aq' : 'Hu (2007) Acta Phys-Chim. Sin 23, 786-789',
 'ar' : '(=q)',
 'as' : 'Wester & Hess (2005) Inorg. Chim. Acta 358, 865-874',
 'at' : 'Urusov (2006) Dokl. Phys-Chem. 408, 169-174',
 'au' : 'Yu & Xue (2006) Acta Cryst. B62, 702',
 'av' : 'Henke (2007) Z. Krist. 222, 477-486',
 'aw' : 'Sidey, Milyan, Semrad & Solomon (2008) J. Alloys Compds. 457, 480',
 'ax' : 'Adams, Moretsky & Canadell (2004) Solid State Ionics, 168, 281',
 'ay' : 'Cabana et al. (2004) Inorg. Chem. 43, 7050',
 'az' : 'Grabowski (2000) J. Mol. Struct. 552, 153',
 'ba' : 'Yu, Xue & Ratajczak (2006) Physica B371, 170',
 'bb' : 'Majerz & Olovsson (2007) Acta Cryst. B63, 650',
 'bc' : 'Brown (2002) The Chemical Bond in Inorganic Chemistry, OUP, p.230',
 'bd' : 'Sidey (2009) Acta Cryst, B65, 99-101',
 'be' : 'Mills, Christy, Chen & Raudsepp, (2009) Z. Krist. 224, 423-431',
 'bf' : 'Diwu, et al. (2010) Inorg Chem. 49 3337-3342',
 'bg' : 'Sidey (2010) Acta Cryst. B66, 307-314',
 'bh' : 'Brown (2009) Acta Cryst. B65, 684-693',
 'bi' : 'Sidey (2012) Private communication',
 'bj' : 'Krivovichev (2012) Z. Krist. 227, 575-579',
 'bk' : 'Mills & Christy (2013) Acta Cryst. B69, 145-149',
 'bl' : 'Palenik & Hu (2009) Inorg. Chim. Acta 362, 4740-4743',
 'bm' : 'Palenik & Hu (2011) Chinese J. Struct. Chem. 30, 1820-1826',
 'bn' : 'Hu, Xie & Palenik (2012) Acta Phys-Chim. Sin. 28, 19-24',
 'bo' : 'Nyman, Rodriguez & Campana (2010) Inorg. Chem. 49, 7748-7755',
 'bp' : 'Sidey, Zubaka, Stercho & Peresh (2010) Chem. Metals Alloys 3, 108-114',
 'bq' : 'Hu (2014) to be published',
 'br' : 'Czervinska, Madura, Zachara (2016) Acta Cryst. B72, 241-248',
 'bs' : 'Gagne, Hawthorne (2015) Acta Cryst. B71, 561-578',
 'bt' : 'J.Rodriguez-Carvajal, Private communication                                     !32',
 'bu' : 'S. Adams and R. Prasada Rao, (2011) Phys. Status Solidi A 208, No. 8, 1746-1753   !33',
 'bv' : 'S. Adams (2013),  Structure and Bonding (eds. Brown & Poeppelmeier) 158, 91-128   !34',
 'bw' : 'Adams S, Moretsky O and Canadell E (2004) Solid State Ionics 168, 281-290         !35'
}

_valence_param_="""
Ac 3   O  -2    2.24     0.37     b   ?
Ac 3   O  -2    2.29     0.35     p   ?
Ac 3   F  -1    2.13     0.37     b   ?
Ac 3   F  -1    2.10     0.40     p   ?
Ac 3   Cl -1    2.63     0.37     b   ?  
Ac 3   Cl -1    2.60     0.40     p   ?
Ac 3   Br -1    2.75     0.40     p   ?
Ag 1   O  -2    1.842    0.37     a   ? 
Ag 1   O  -2    1.875    0.359    bs  ? 
Ag 1   O  -2    1.805    0.37     b   ?
Ag 1   S  -2    2.119    0.37     a   ? 
Ag 1   F  -1    1.80     0.37     b   ? 
Ag 1   Cl -1    2.09     0.37     b   ?
Ag 2   F  -1    1.79     0.37     e   unchecked
Ag 3   F  -1    1.83     0.37     e   unchecked
Ag 9   Br -1    2.22     0.37     b   ?  
Ag 9   I  -1    2.38     0.37     b   ?
Ag 9   Se -2    2.26     0.37     b   ? 
Ag 9   Te -2    2.51     0.37     b   ?
Ag 9   N  -3    1.85     0.37     b   ?
Ag 9   P  -3    2.22     0.37     b   ?
Ag 9   As -3    2.30     0.37     b   ?
Ag 9   H  -1    1.50     0.37     b   ?
Al 3   O  -2    1.651    0.37     a   ?
Al 3   O  -2    1.634    0.390    bs  ?
Al 3   O  -2    1.644    0.38     o   ? 
Al 3   S  -2    2.21     0.37     e   unchecked
Al 3   S  -2    2.13     0.37     b   ?
Al 3   Se -2    2.27     0.37     b   ?
Al 3   Te -2    2.48     0.37     b   ? 
Al 3   F  -1    1.545    0.37     a   ?  
Al 3   Cl -1    2.032    0.37     a   ? 
Al 3   Br -1    2.20     0.37     b   ?
Al 3   I  -1    2.41     0.37     b   ? 
Al 3   N  -3    1.79     0.37     b   ?
Al 3   P  -3    2.24     0.37     b   ?
Al 3   As -3    2.30     0.37     b   ?
Al 3   H  -1    1.45     0.37     b   ?
Am 3   O  -2    2.11     0.37     b   ?           
Am 3   O  -2    2.068    0.392    bs  'sample of one'           
Am 3   O  -2    2.13     0.35     p   ?
Am 3   F  -1    2.00     0.37     b   ? 
Am 3   F  -1    1.98     0.40     p   ?
Am 3   Cl -1    2.48     0.37     b   ?
Am 3   Cl -1    2.45     0.40     p   ?
Am 3   Br -1    2.59     0.40     p   ?
Am 4   O  -2    2.08     0.37     p   ?
Am 4   O  -2    2.12     0.37     e   unchecked
Am 4   F  -1    1.96     0.40     p   ?
Am 5   O  -2    2.07     0.35     p   ?
Am 5   F  -1    1.95     0.40     p   ?
Am 6   O  -2    2.05     0.35     p   ?
Am 6   F  -1    1.95     0.40     p   ?
Am 5   O  -2    2.12     0.37     e   unchecked
As 2   S  -2    2.24     0.37     e   unchecked
As 2   Se -2    2.38     0.37     e   unchecked
As 3   O  -2    1.74     0.50     e   ?
As 3   O  -2    1.775    0.423    bs  ?
As 3   O  -2    1.789    0.37     a   ?
As 3   S  -2    2.272    0.37     a   ? 
As 3   Se -2    2.40     0.37     e   unchecked 
As 3   Te -2    2.65     0.37     e   unchecked
As 3   F  -1    1.70     0.37     b   ?
As 3   Cl -1    2.16     0.37     b   ? 
As 3   Br -1    2.35     0.37     e   unchecked
As 3   I  -1    2.58     0.37     e   unchecked
As 3   C  -4    1.93     0.37     b   ?
As 5   O  -2    1.767    0.37     a   ?
As 5   O  -2    1.765    0.352    bs  ?
As 5   S  -2    2.28     0.37     e   unchecked
As 5   F  -1    1.620    0.37     a   ?
As 5   Cl -2    2.14     0.37     b   ?
Au 1   Cl -1    2.02     0.37     e   unchecked 
Au 1   I  -1    2.35     0.37     e   unchecked
Au 3   O  -2    1.89     0.37     e   ?
Au 3   O  -2    1.833    0.37     b   ?
Au 3   O  -2    1.890    0.375    bs  ?
Au 3   S  -2    2.39     0.35     e   unchecked 
Au 3   F  -1    1.89     0.37     e   unchecked
Au 3   F  -1    1.81     0.37     b   ?
Au 3   Cl -1    2.17     0.37     b   ? 
Au 3   Br -1    2.32     0.37     e   unchecked
Au 3   I  -1    2.54     0.37     e   unchecked
Au 3   N  -3    1.94     0.35     e   unchecked
Au 5   F  -1    1.80     0.37     e   unchecked
Au 9   S  -2    2.03     0.37     b   ?
Au 9   Se -2    2.18     0.37     b   ?
Au 9   Te -2    2.41     0.37     b   ?
Au 9   Br -1    2.12     0.37     b   ?
Au 9   I  -1    2.34     0.37     b   ? 
Au 9   N  -3    1.72     0.37     b   ?
Au 9   P  -3    2.14     0.37     b   ?
Au 9   As -3    2.22     0.37     b   ?
Au 9   H  -1    1.37     0.37     b   ?
B  3   O  -2    1.371    0.37     a   ?
B  3   O  -2    1.372    0.357    bs  ?
B  3   O  -2    1.364    0.37     br  ?
B  3   S  -2    1.815    0.37     au  ?
B  3   S  -2    1.82     0.37     b   ?
B  3   Se -2    1.95     0.37     b   ? 
B  3   Te -2    2.20     0.37     b   ?
B  3   F  -1    1.281    0.37     a   ?
B  3   F  -1    1.289    0.37     au  ?
B  3   F  -1    1.31     0.37     b   ? 
B  3   Cl -1    1.74     0.37     b   ? 
B  3   Br -1    1.88     0.37     b   ? 
B  3   I  -1    2.10     0.37     b   ? 
B  3   N  -3    1.482    0.37     au  ?
B  3   N  -3    1.47     0.37     b   ?
B  3   P  -3    1.920    0.37     au  ?
B  3   P  -3    1.88     0.37     b   ?
B  3   As -3    1.97     0.37     b   ?
B  3   H  -1    1.14     0.37     b   ? 
B  3   C  -4    1.569    0.28     br  ?
B  3   B   3    1.402    0.37     e   unchecked
Ba 2   O  -2    2.285    0.37     a   ?
Ba 2   O  -2    2.223    0.406    bs  ?
Ba 2   S  -2    2.769    0.37     a   ? 
Ba 2   Se -2    2.88     0.37     b   ?
Ba 2   Te -2    3.08     0.37     b   ? 
Ba 2   F  -1    2.188    0.37     a   ? 
Ba 2   Cl -1    2.69     0.37     b   ? 
Ba 2   Br -1    2.88     0.37     b   ? 
Ba 2   I  -1    3.13     0.37     b   ? 
Ba 2   N  -3    2.47     0.37     b   ?
Ba 2   P  -3    2.88     0.37     b   ?
Ba 2   As -3    2.96     0.37     b   ?
Ba 2   H  -1    2.22     0.37     b   ?
Be 2   O  -2    1.381    0.37     a   ? 
Be 2   O  -2    1.429    0.297    bs  ? 
Be 2   S  -2    1.83     0.37     b   ? 
Be 2   Se -2    1.97     0.37     b   ? 
Be 2   Te -2    2.21     0.37     b   ?
Be 2   F  -1    1.281    0.37     a   ? 
Be 2   Cl -1    1.76     0.37     b   ? 
Be 2   Br -1    1.90     0.37     b   ? 
Be 2   I  -1    2.10     0.37     b   ? 
Be 2   N  -3    1.50     0.37     b   ?
Be 2   P  -3    1.95     0.37     b   ?
Be 2   As -3    2.00     0.37     b   ?
Be 2   H  -1    1.11     0.37     b   ?
Bi 3   O  -2    1.990    0.48     bj  ?
Bi 3   O  -2    2.068    0.389    bs  ?
Bi 3   O  -2    2.094    0.37     a   ? 
Bi 3   S  -2    2.570    0.37     a   ? 
Bi 3   Se -2    2.70     0.35     e   unchecked 
Bi 3   F  -1    1.99     0.37     b   ?
Bi 3   Cl -1    2.48     0.37     b   ? 
Bi 3   Cl -1    2.40     0.37     e   unchecked
Bi 3   Br -1    2.597    0.37     ak  ?
Bi 3   Br -1    2.567    0.421    ak  'R0 from gas phase, small sample' 
Bi 3   I  -1    2.82     0.37     e   unchecked
Bi 3   N  -3    2.02     0.35     e   unchecked
Bi 5   O  -2    2.06     0.37     b   ?
Bi 5   O  -2    2.050    0.318    bs  ?
Bi 5   F  -1    1.97     0.37     b   ? 
Bi 5   Cl -1    2.44     0.37     b   ?
Bi 9   Br -1    2.62     0.37     b   ?
Bi 9   I  -1    2.84     0.37     b   ?
Bi 9   S  -2    2.55     0.37     b   ?
Bi 9   Se -2    2.72     0.37     b   ?
Bi 9   Te -2    2.87     0.37     b   ?
Bi 9   N  -3    2.24     0.37     b   ?
Bi 9   P  -3    2.63     0.37     b   ?
Bi 9   As -3    2.72     0.37     b   ?
Bi 9   H  -1    1.97     0.37     b   ?
Bk 3   O  -2    2.08     0.37     b   ?
Bk 3   O  -2    2.10     0.35     p   ?
Bk 3   F  -1    1.96     0.37     b   ?
Bk 3   F  -1    1.95     0.40     p   ?
Bk 3   Cl -1    2.35     0.37     e   unchecked
Bk 3   Cl -1    2.46     0.37     b   ?
Bk 3   Cl -1    2.42     0.40     p   ?
Bk 3   Br -1    2.56     0.40     p   ?
Bk 4   O  -2    2.07     0.35     p   ?
Bk 4   F  -1    1.93     0.40     p   ?
Br 3   O  -2    1.90     0.37     e   unchecked           
Br 3   F  -1    1.75     0.37     e   unchecked
Br 5   O  -2    1.890    0.571    bs  ?
Br 5   O  -2    1.84     0.37     e   unchecked
Br 5   F  -1    1.76     0.37     e   unchecked
Br 7   O  -2    1.81     0.37     b   ?
Br 7   O  -2    1.850    0.428    bs  'sample of two'
Br 7   F  -1    1.72     0.37     b   ?
Br 7   Cl -1    2.19     0.37     b   ?
C  2   O  -2    1.366    0.37     e   unchecked                   
C  2   Cl -1    1.410    0.37     e   unchecked
C  4   O  -2    1.390    0.37     a   ?
C  4   O  -2    1.398    0.399    bs  ?
C  4   O  -2    1.407    0.37     au  'small sample'
C  4   O  -2    1.40     0.26     o   ? 
C  4   C   4    1.54     0.37     e   ?
C  4   S  -2    1.80     0.37     e   unchecked
C  4   F  -1    1.32     0.37     b   ?
C  4   F  -1    1.41     0.37     e   unchecked
C  4   Cl -1    1.76     0.37     b   ?
C  4   Br -1    1.91     0.37     e   unchecked 
C  4   N  -3    1.442    0.37     a   ?
C  9   Se -2    1.97     0.37     b   ?
C  9   I  -1    2.12     0.37     b   ?
C  9   Br -1    1.90     0.37     b   ?
C  9   S  -2    1.82     0.37     b   ?
C  9   Te -2    2.21     0.37     b   ?
C  9   N  -3    1.47     0.37     b   ?
C  9   P  -3    1.89     0.37     b   ?
C  9   As -3    1.99     0.37     b   ?
C  9   H  -1    1.10     0.37     b   ?
Ca 2   O  -2    1.967    0.37     a   ? 
Ca 2   O  -2    1.907    0.409    bs  ? 
Ca 2   O  -2    1.896    0.41     o   ? 
Ca 2   S  -2    2.45     0.37     b   ? 
Ca 2   Se -2    2.56     0.37     b   ?
Ca 2   Te -2    2.76     0.37     b   ? 
Ca 2   F  -1    1.842    0.37     a   ? 
Ca 2   Cl -1    2.37     0.37     b   ? 
Ca 2   Br -1    2.507    0.37     e   unchecked
Ca 2   Br -1    2.49     0.37     b   ?
Ca 2   I  -1    2.72     0.37     b   ? 
Ca 2   N  -3    2.14     0.37     b   ? 
Ca 2   P  -3    2.55     0.37     b   ?
Ca 2   As -3    2.62     0.37     b   ?
Ca 2   H  -1    1.83     0.37     b   ?
Cd 2   O  -2    1.904    0.37     a   ?
Cd 2   O  -2    1.827    0.430    bs  ?
Cd 2   O  -2    1.875    0.37     ao  ?
Cd 2   S  -2    2.304    0.37     a   ? 
Cd 2   S  -2    2.279    0.37     ao  ?
Cd 2   Se -2    2.40     0.37     b   ?
Cd 2   Te -2    2.59     0.37     b   ? 
Cd 2   F  -1    1.811    0.37     b   ? 
Cd 2   Cl -1    2.212    0.37     a   ?
Cd 2   Cl -1    2.23     0.37     b   ? 
Cd 2   Cl -1    2.22     0.37     ao  ?
Cd 2   Br -1    2.334    0.37     ao  ?
Cd 2   Br -1    2.35     0.37     b   ?
Cd 2   I  -1    2.525    0.37     ao  ?
Cd 2   I  -1    2.57     0.37     b   ?
Cd 2   I  -1    2.60     0.37     e   unchecked
Cd 2   N  -3    1.96     0.37     b   ?
Cd 2   N  -3    1.951    0.37     ao  ?
Cd 2   P  -3    2.34     0.37     b   ?
Cd 2   As -3    2.43     0.37     b   ?
Cd 2   H  -1    1.66     0.37     b   ?
Ce 3   O  -2    2.151    0.37     b   ?
Ce 3   O  -2    2.114    0.389    bs  ?
Ce 3   O  -2    2.118    0.37     bl  'in trans-metal compleses'
Ce 3   O  -2    2.121    0.37     ab  'in trans-metal complexes'
Ce 3   O  -2    2.116    0.37     ae  'in trans-metal complexes'
Ce 3   S  -2    2.602    0.37     al  ?
Ce 3   S  -2    2.65     0.37     e   unchecked
Ce 3   F  -1    2.036    0.37     b   ?
Ce 3   F  -1    2.251    0.37     bl  'in trans-metal complexes'
Ce 3   F  -1    2.00     0.40     p   ?
Ce 3   Cl -1    2.52     0.37     b   ?
Ce 3   Cl -1    2.49     0.40     p   ?
Ce 3   Cl -1    2.54     0.37     al  ?
Ce 3   Br -1    2.65     0.35     e   ?
Ce 3   Br -1    2.65     0.40     p   ?
Ce 3   I  -1    2.87     0.40     p   ?
Ce 4   O  -2    2.028    0.37     b   ?
Ce 4   O  -2    2.046    0.416    bs  ?
Ce 4   O  -2    2.070    0.37     bl  'in trans-metal complexes'
Ce 4   O  -2    2.068    0.37     ab  'in organic compounds'
Ce 4   O  -2    2.074    0.37     al  ?
Ce 4   S  -2    2.65     0.35     e   unchecked
Ce 4   F  -1    1.995    0.37     b   ?
Ce 4   F  -1    1.97     0.40     p   ?
Ce 4   N  -3    2.179    0.37     al  ?
Ce 4   N  -3    2.202    0.37     bl  'in trans-metal complexes'
Ce 9   Cl -1    2.41     0.37     b   ?
Ce 9   Br -1    2.69     0.37     b   ?
Ce 9   I  -1    2.92     0.37     b   ? 
Ce 9   S  -2    2.62     0.37     b   ?
Ce 9   Se -2    2.74     0.37     b   ? 
Ce 9   Te -2    2.92     0.37     b   ?
Ce 9   N  -3    2.254    0.37     ah  ?
Ce 9   N  -3    2.34     0.37     b   ?
Ce 9   P  -3    2.70     0.37     b   ?
Ce 9   As -3    2.78     0.37     b   ?
Ce 9   H  -1    2.04     0.37     b   ?
Cf 3   O  -2    2.07     0.37     b   ?
Cf 3   F  -1    1.95     0.37     b   ?
Cf 3   F  -1    1.94     0.40     p   ?
Cf 3   Cl -1    2.45     0.37     b   ?
Cf 3   Cl -1    2.41     0.40     p   ?
Cf 3   Br -1    2.55     0.40     p   ?
Cf 4   O  -2    2.06     0.35     p   ?
Cf 4   F  -1    1.92     0.40     p   ?
Cl 3   O  -2    1.722    0.37     bs  ?
Cl 3   O  -2    1.71     0.37     e   unchecked      
Cl 3   F  -1    1.69     0.37     e   unchecked
Cl 5   O  -2    1.703    0.428    bs  ?
Cl 5   O  -2    1.67     0.37     e   unchecked
Cl 7   O  -2    1.632    0.37     a   ?   
Cl 7   O  -2    1.669    0.428    bs  ?   
Cl 7   F  -1    1.55     0.37     b   ? 
Cl 7   Cl -1    2.00     0.37     b   ?
Cf 3   Cl -1    2.45     0.37     b   ?
Cm 3   O  -2    2.23     0.37     b   ?
Cm 3   O  -2    2.12     0.35     p   ?
Cm 3   F  -1    2.12     0.37     b   ?
Cm 3   F  -1    1.96     0.40     p   ?
Cm 3   Cl -1    2.62     0.37     b   ?
Cm 3   Cl -1    2.44     0.40     p   ?
Cm 4   O  -2    2.08     0.35     p   ?
Cm 4   O  -2    2.034    0.412    bs  'sample of one'
Cm 4   F  -1    1.94     0.40     p   ?
Co 1   H  -1    1.000    0.35     e   unchecked
Co 2   O  -2    1.692    0.37     a   ?
Co 2   O  -2    1.698    0.376    bs  ?
Co 2   O  -2    1.685    0.37     i   'from transition metal complexes'
Co 2   S  -2    1.94     0.37     e   unchecked
Co 2   F  -1    1.64     0.37     b   ?
Co 2   Cl -1    2.033    0.37     a   ?
Co 2   Cl -1    2.01     0.37     b   ? 
Co 2   N  -3    1.72     0.37     bq  'high spin'
Co 2   N  -3    1.60     0.37     bq  'low spin'
Co 3   O  -2    1.637    0.37     i   'from transition metal complexes'
Co 3   O  -2    1.655    0.364    bs  ?
Co 3   O  -2    1.70     0.37     b   ? 
Co 3   S  -2    2.02     0.37     e   unchecked 
Co 3   F  -1    1.62     0.37     b   ?
Co 3   Cl -1    2.05     0.37     b   ?           
Co 3   N  -3    1.69     0.37     bq  'low spin'
Co 3   C   2    1.634    0.37     b   ?
Co 4   O  -2    1.729    0.358    bs  'sample of one'
Co 4   O  -2    1.72     0.37     e   unchecked      
Co 4   F  -1    1.55     0.37     e   unchecked
Co 9   O  -2    1.655    0.42     o   ?
Co 9   Br -1    2.18     0.37     b   ? 
Co 9   I  -1    2.37     0.35     b   ? 
Co 9   S  -2    2.06     0.37     b   ?
Co 9   Se -2    2.24     0.37     b   ? 
Co 9   Te -2    2.46     0.37     b   ?
Co 9   N  -3    1.84     0.37     b   ?
Co 9   P  -3    2.21     0.37     b   ?
Co 9   As -3    2.28     0.37     b   ?
Co 9   H  -1    1.44     0.37     b   ?
Cr 2   O  -2    1.761    0.350    bs  ?
Cr 2   O  -2    1.73     0.37     b   ?
Cr 2   F  -1    1.67     0.37     b   ?
Cr 2   F  -1    1.74     0.37     e   unchecked
Cr 2   Cl -1    2.09     0.37     b   ?
Cr 2   Br -1    2.26     0.37     e   unchecked
Cr 2   I  -1    2.48     0.37     e   unchecked
Cr 2   N  -3    1.80     0.37     bq  'low spin'
Cr 2   N  -3    1.86     0.37     bq  'high spin'
Cr 3   O  -2    1.724    0.37     a   ?
Cr 3   O  -2    1.725    0.361    bs  ?
Cr 3   O  -2    1.708    0.37     w   'from transition metal complexes'
Cr 3   S  -2    2.162    0.37     e   unchecked
Cr 3   F  -1    1.657    0.37     a   ?
Cr 3   F  -1    1.64     0.37     b   ?
Cr 3   Cl -1    2.08     0.37     b   ? 
Cr 3   Br -1    2.28     0.37     e   unchecked
Cr 3   N  -3    1.78     0.37     bq  'high spin'
Cr 4   O  -2    1.783    0.410    bs  ?
Cr 4   O  -2    1.81     0.37     e   unchecked
Cr 4   F  -1    1.56     0.37     e   unchecked
Cr 5   O  -2    1.76     0.37     w   'from transition metal complexes'
Cr 5   O  -2    1.777    0.375    bs  ?
Cr 6   O  -2    1.794    0.37     a   ?   
Cr 6   O  -2    1.709    0.375    bs  ?   
Cr 6   F  -1    1.74     0.37     b   ? 
Cr 6   Cl -1    2.12     0.37     b   ?
Cr 9   O  -2    1.79     0.34     o   ?
Cr 9   O  -2    1.724    0.37     w   'from transition metal complexes'
Cr 9   Br -1    2.26     0.37     b   ?
Cr 9   I  -1    2.45     0.37     b   ? 
Cr 9   S  -2    2.18     0.37     b   ?
Cr 9   Se -2    2.29     0.37     b   ? 
Cr 9   Te -2    2.52     0.37     b   ?
Cr 9   N  -3    1.85     0.37     b   ?
Cr 9   P  -3    2.27     0.37     b   ?
Cr 9   As -3    2.34     0.37     b   ?
Cr 9   H  -1    1.52     0.37     b   ?
Cs 1   O  -2    2.417    0.37     a   ?
Cs 1   O  -2    2.296    0.411    bs  ?
Cs 1   O  -2    2.2862   0.408    c   '7 A cut-off' 
Cs 1   S  -2    2.89     0.37     b   ?
Cs 1   S  -2    2.5253   0.517    c   '7 A cut-off'
Cs 1   S  -2    2.93     0.37     e   unchecked
Cs 1   Se -2    2.98     0.37     b   ?
Cs 1   Se -2    2.6424   0.553    c   '7 A cut-off'
Cs 1   Te -2    3.16     0.37     b   ?
Cs 1   Te -2    2.7647   0.603    c   '8 A cut-off'
Cs 1   F  -1    2.33     0.37     b   ?
Cs 1   F  -1    2.1980   0.410    c   '7 A cut-off'
Cs 1   F  -1    2.38     0.37     e   unchecked
Cs 1   Cl -1    2.791    0.37     a   ?
Cs 1   Cl -1    2.4715   0.495    c   '7 A cut-off'
Cs 1   Br -1    2.95     0.37     b   ?
Cs 1   Br -1    2.5035   0.543    c   '7 A cut-off'
Cs 1   I  -1    3.18     0.37     b   ? 
Cs 1   I  -1    2.6926   0.609    c   '8 A cut-off'
Cs 1   I  -1    3.29     0.37     e   unchecked
Cs 1   N  -3    2.83     0.37     e   unchecked
Cs 1   N  -3    2.53     0.37     b   ?
Cs 1   P  -3    2.93     0.37     b   ? 
Cs 1   As -3    3.04     0.37     b   ? 
Cs 1   H  -1    2.44     0.37     b   ? 
Cu 1   O  -2    1.610    0.37     e   unchecked
Cu 1   O  -2    1.601    0.335    bs  ?
Cu 1   O  -2    1.504    0.37     l   'from transition metal complexes'
Cu 1   S  -2    1.898    0.37     a   ?
Cu 1   S  -2    1.811    0.37     l   'from transition metal complexes'
Cu 1   Se -2    1.900    0.37     l   'from transition metal complexes'
Cu 1   F  -1    1.6      0.37     b   ? 
Cu 1   Cl -1    1.858    0.37     l   'from transition metal complexes'
Cu 1   Cl -1    1.89     0.37     e   unchecked
Cu 1   Br -1    2.03     0.37     e   unchecked
Cu 1   I  -1    2.108    0.37     a   ?
Cu 1   I  -1    2.155    0.37     l   'from transition metal complexes'
Cu 1   N  -3    1.520    0.37     l   '3-coordinate N'
Cu 1   N  -3    1.480    0.37     l   '2-coordinate N'
Cu 1   N  -3    1.630    0.37     l   '4-coordinate N'
Cu 1   P  -3    1.774    0.37     l   'from transition metal complexes'
Cu 1   As -3    1.856    0.37     l   'from transition metal complexes'
Cu 1   C  -4    1.446    0.37     l   'from transition metal complexes'
Cu 2   O  -2    1.679    0.36     bj  ?
Cu 2   O  -2    1.687    0.355    bs  ?
Cu 2   O  -2    1.679    0.37     a   ?
Cu 2   O  -2    1.649    0.37     j   'from transition metal complexes'
Cu 2   O  -2    1.655    0.37     l   'from transition metal complexes'
Cu 2   S  -2    2.054    0.37     a   ?
Cu 2   S  -2    2.060    0.37     j   'from transition metal complexes'
Cu 2   S  -2    2.024    0.37     l   'from transition metal complexes'
Cu 2   S  -2    1.86     0.37     b   ? 
Cu 2   Se -2    2.02     0.37     b   ?
Cu 2   Se -2    2.124    0.37     l   ? 
Cu 2   Te -2    2.27     0.37     b   ? 
Cu 2   F  -1    1.594    0.37     a   ?
Cu 2   Cl -1    2.00     0.37     b   ?      
Cu 2   Br -1    1.99     0.37     b   ?
Cu 2   Br -1    2.134    0.37     l   'from transition metal complexes'
Cu 2   I  -1    2.16     0.37     b   ?
Cu 2   I  -1    2.36     0.37     l   'from transition metal complexes'
Cu 2   N  -3    1.751    0.37     j   'from transition metal complexes'
Cu 2   N  -3    1.713    0.37     l   'from transition metal complexes'
Cu 2   N  -3    1.61     0.37     b   ?
Cu 2   N  -3    1.709    0.37     l   '2-coordinate N'
Cu 2   N  -3    1.704    0.37     l   '3-coordinate N'
Cu 2   N  -3    1.763    0.37     l   '4-coordinate N'
Cu 2   P  -3    1.97     0.37     b   ?
Cu 2   P  -3    2.05     0.37     l   'from transition metal complexes'
Cu 2   As -3    2.08     0.37     b   ?
Cu 2   C  -4    1.72     0.37     l   'from transition metal complexes'
Cu 2   H  -1    1.21     0.37     b   ? 
Cu 3   O  -2    1.735    0.37     t   ?
Cu 3   O  -2    1.737    0.375    bs  ?
Cu 3   O  -2    1.739    0.37     e   unchecked      
Cu 3   F  -1    1.58     0.37     e   unchecked
Cu 3   Cl -1    2.078    0.37     l   'from transition metal complexes'
Cu 3   N  -3    1.768    0.37     l   'from transition metal complexes'
Cu 3   N  -3    1.753    0.37     t   ?
Cu 3   C  -4    1.84     0.37     l   'from transition metal complexes'
Dy 2   O  -2    1.90     0.37     e   unchecked
Dy 3   O  -2    2.001    0.37     a   ?
Dy 3   O  -2    2.002    0.389    bs  ?
Dy 3   O  -2    2.005    0.37     ae  'from transition metal complexes'
Dy 3   F  -1    1.922    0.37     b   ?
Dy 3   F  -1    1.89     0.40     p   ?
Dy 3   Cl -1    2.410    0.37     b   ?
Dy 3   Cl -1    2.38     0.40     p   ?
Dy 3   Cl -1    2.407    0.37     al  ?
Dy 3   Br -1    2.53     0.40     p   ?
Dy 3   I  -1    2.76     0.40     p   ?
Dy 9   Br -1    2.56     0.37     b   ?
Dy 9   I  -1    2.77     0.37     b   ?
Dy 9   S  -2    2.47     0.37     b   ?
Dy 9   S  -2    2.473    0.37     al  ? 
Dy 9   Se -2    2.61     0.37     b   ? 
Dy 9   Te -2    2.80     0.37     b   ?
Dy 9   N  -3    2.124    0.37     ah  ?
Dy 9   N  -3    2.18     0.37     b   ?
Dy 9   P  -3    2.57     0.37     b   ?
Dy 9   As -3    2.64     0.37     b   ?
Dy 9   H  -1    1.89     0.37     b   ?
Er 2   O  -2    1.88     0.37     e   unchecked
Er 2   S  -2    2.52     0.37     e   unchecked
Er 3   O  -2    1.988    0.37     a   ?
Er 3   O  -2    1.991    0.373    bs  ?
Er 3   O  -2    2.010    0.37     b   ?
Er 3   O  -2    1.979    0.37     ae  'from transition metal complexes'
Er 3   S  -2    2.475    0.37     al  ?
Er 3   Se -2    2.58     0.37     e   unchecked
Er 3   F  -1    1.904    0.37     a   ?
Er 3   F  -1    1.87     0.40     p   ?
Er 3   Cl -1    2.390    0.37     b   ?
Er 3   Cl -1    2.385    0.37     al  ?
Er 3   Cl -1    2.36     0.40     p   ?
Er 3   Br -1    2.51     0.40     p   ?
Er 3   I  -1    2.75     0.40     p   ?
Er 9   Br -1    2.54     0.37     b   ? 
Er 9   I  -1    2.75     0.37     b   ? 
Er 9   S  -2    2.46     0.37     b   ? 
Er 9   Se -2    2.59     0.37     b   ? 
Er 9   Te -2    2.78     0.37     b   ?
Er 9   N  -3    2.086    0.37     ah  ?
Er 9   N  -3    2.16     0.37     b   ?
Er 9   P  -3    2.55     0.37     b   ? 
Er 9   As -3    2.63     0.37     b   ? 
Er 9   H  -1    1.86     0.37     b   ?
Es 3   O  -2    2.08     0.35     p   ? 
Eu 2   O  -2    2.147    0.37     b   ?
Eu 2   O  -2    2.102    0.37     al  ?
Eu 2   O  -2    1.943    0.490    bs  'small sample'
Eu 2   S  -2    2.584    0.37     a   ?
Eu 2   F  -1    2.04     0.37     b   ? 
Eu 2   Cl -1    2.53     0.37     b   ? 
Eu 2   Br -1    2.67     0.37     e   unchecked
Eu 2   I  -1    2.90     0.37     e   unchecked
Eu 2   N  -3    2.16     0.37     al  ?
Eu 3   O  -2    2.074    0.37     a   ?
Eu 3   O  -2    2.068    0.359    bs  ?
Eu 3   O  -2    2.038    0.37     ae  'from transition metal complexes'
Eu 3   S  -2    2.509    0.37     al  ?
Eu 3   F  -1    1.961    0.37     b   ?
Eu 3   F  -1    1.93     0.40     p   ?
Eu 3   Cl -1    2.455    0.37     b   ?
Eu 3   Cl -1    2.468    0.37     al  ?
Eu 3   Cl -1    2.42     0.40     p   ?
Eu 3   Br -1    2.57     0.40     p   ?
Eu 3   I  -1    2.79     0.40     p   ?
Eu 9   Br -1    2.61     0.37     b   ? 
Eu 9   I  -1    2.83     0.37     b   ? 
Eu 9   S  -2    2.53     0.37     b   ? 
Eu 9   Se -2    2.66     0.37     b   ? 
Eu 9   Te -2    2.85     0.37     b   ?
Eu 9   N  -3    2.161    0.37     ah  ?  
Eu 9   N  -3    2.24     0.37     b   ? 
Eu 9   P  -3    2.62     0.37     b   ? 
Eu 9   As -3    2.70     0.37     b   ? 
Eu 9   H  -1    1.95     0.37     b   ? 
Fe 2   O  -2    1.734    0.37     a   ?
Fe 2   O  -2    1.658    0.447    bs  ?
Fe 2   O  -2    1.713    0.37     h   ?
Fe 2   O  -2    1.700    0.37     j   ?
Fe 2   S  -2    2.12     0.37     e   unchecked
Fe 2   S  -2    2.125    0.37     j   'from transition metal complexes'
Fe 2   F  -1    1.65     0.37     b   ?
Fe 2   Cl -1    2.06     0.37     b   ?
Fe 2   Cl -1    2.15     0.37     e   unchecked
Fe 2   Br -1    2.21     0.35     e   unchecked
Fe 2   I  -1    2.47     0.35     e   ?
Fe 2   N  -3    1.76     0.37     bq  'high spin'
Fe 2   N  -3    1.66     0.37     bq  'intermediate spin'
Fe 2   N  -3    1.56     0.37     bq  'low spin'
Fe 2   N  -3    1.769    0.37     j   'from transition metal complexes'
Fe 3   O  -2    1.759    0.37     a   ?
Fe 3   O  -2    1.766    0.360    bs  ?
Fe 3   O  -2    1.751    0.37     h   'from transition metal complexes'
Fe 3   O  -2    1.765    0.37     j   'from transition metal complexes'
Fe 3   S  -2    2.149    0.37     a   ?
Fe 3   S  -2    2.134    0.37     j   ?
Fe 3   F  -1    1.679    0.37     a   ? 
Fe 3   Cl -1    2.09     0.37     b   ?
Fe 3   Cl -1    2.15     0.37     e   unchecked 
Fe 3   Br -1    2.22     0.37     e   ?
Fe 3   N  -3    1.82     0.37     bq  'high spin'
Fe 3   N  -3    1.70     0.37     bq  'low spin'
Fe 3   N  -3    1.815    0.37     j   'from transition metal complexes'
Fe 3   C   2    1.689    0.37     a   ?
Fe 4   S  -2    2.23     0.35     e   unchecked
Fe 6   O  -2    1.76     0.35     e   unchecked
Fe 9   O  -2    1.795    0.30     ag  'for all oxidation states'
Fe 9   O  -2    1.74     0.38     o   ?
Fe 9   Br -1    2.26     0.37     b   ?
Fe 9   I  -1    2.47     0.37     b   ?
Fe 9   S  -2    2.16     0.37     b   ?
Fe 9   Se -2    2.28     0.37     b   ?
Fe 9   Te -2    2.53     0.37     b   ?
Fe 9   N  -3    1.86     0.37     b   ?
Fe 9   P  -3    2.27     0.37     b   ?
Fe 9   As -3    2.35     0.37     b   ?
Fe 9   H  -1    1.53     0.37     b   ?
Ga 1   Se -1    2.55     0.37     e   unchecked
Ga 3   O  -2    1.730    0.37     a   ?
Ga 3   O  -2    1.736    0.345    bs  ?
Ga 3   S  -2    2.163    0.37     a   ? 
Ga 3   F  -1    1.62     0.37     b   ?
Ga 3   F  -1    1.69     0.37     e   unchecked
Ga 3   Cl -1    2.07     0.37     b   ?
Ga 3   Br -1    2.20     0.35     e   ? 
Ga 3   I  -1    2.46     0.37     e   unchecked
Ga 9   Br -1    2.24     0.37     b   ?
Ga 9   I  -1    2.45     0.37     b   ?
Ga 9   S  -2    2.17     0.37     b   ?
Ga 9   Se -2    2.30     0.37     b   ?
Ga 9   Te -2    2.54     0.37     b   ?
Ga 9   N  -3    1.84     0.37     b   ?
Ga 9   P  -3    2.26     0.37     b   ?
Ga 9   As -3    2.34     0.37     b   ?
Ga 9   H  -1    1.51     0.37     b   ?
Gd 2   O  -2    2.01     0.37     e   unchecked
Gd 2   F  -1    2.40     0.37     e   unchecked
Gd 3   O  -2    2.065    0.37     b   ?
Gd 3   O  -2    1.988    0.433    bs  ?
Gd 3   O  -2    2.031    0.37     ae  'from transition metal complexes'
Gd 3   S  -2    2.53     0.37     e   unchecked
Gd 3   F  -1    1.95     0.37     b   ?
Gd 3   F  -1    1.92     0.40     p   ?
Gd 3   Cl -1    2.445    0.37     b   ?
Gd 3   Cl -1    2.41     0.40     p   ?
Gd 3   Cl -1    2.457    0.37     al  ?
Gd 3   Br -1    2.56     0.40     p   ?
Gd 3   I  -1    2.78     0.40     p   ?
Gd 9   Br -1    2.60     0.37     b   ?
Gd 9   I  -1    2.82     0.37     b   ?
Gd 9   S  -2    2.53     0.37     b   ?
Gd 9   S  -2    2.518    0.37     al  ?
Gd 9   Se -2    2.65     0.37     b   ? 
Gd 9   Te -2    2.84     0.37     b   ?
Gd 9   N  -3    2.146    0.37     ah  ?
Gd 9   N  -3    2.22     0.37     b   ?
Gd 9   N  -3    2.10     0.37     e   ?
Gd 9   P  -3    2.61     0.37     b   ?
Gd 9   As -3    2.68     0.37     b   ?
Gd 9   H  -1    1.93     0.37     b   ?
Ge 2   S  -2    2.15     0.50     e   ?
Ge 4   O  -2    1.748    0.37     a   ?
Ge 4   O  -2    1.750    0.363    bs  ?
Ge 4   S  -2    2.217    0.37     a   ? 
Ge 4   Se -2    2.35     0.37     e   unchecked
Ge 4   F  -1    1.66     0.37     b   ?
Ge 4   Cl -1    2.14     0.37     b   ? 
Ge 9   Br -1    2.30     0.37     b   ? 
Ge 9   I  -1    2.50     0.37     b   ? 
Ge 9   S  -2    2.23     0.37     b   ? 
Ge 9   Se -2    2.35     0.37     b   ?  
Ge 9   Te -2    2.56     0.37     b   ? 
Ge 9   N  -3    1.88     0.37     b   ?
Ge 9   P  -3    2.32     0.37     b   ? 
Ge 9   As -3    2.43     0.37     b   ? 
Ge 9   H  -1    1.55     0.37     b   ?
H  1   O  -2    0.569    0.94     bc  '1.05<O-H<1.70 A, best general value'
H  1   O  -2    0.907    0.28     bc  'O-H < 1.05 A'
H  1   O  -2    0.990    0.59     bc  '1.70 A < O-H'
H  1   O  -2    0.918    0.427    bs  ?
H  1   O  -2    0.925    0.40     az  ?
H  1   O  -2    0.957    0.35     az  'From gas and symmetrical bond length'
H  1   O  -2    0.870    0.457    ax  '4.0 A cut-off, b determined from softness'
H  1   O  -2    0.790    0.37     ba  'For s > 0.5 vu'
H  1   O  -2    1.409    0.37     ba  'For s < 0.5 vu'
H  1   S  -2    1.192    0.591    ax  '5.5 A cut-off, b determined from softness'
H  1   F  -1    0.708    0.558    ax  '4.5 A cut-off, b determined from softness'
H  1   Cl -1    1.336    0.53     am  ?
H  1   N  -3    1.014    0.413    bb  'From gas and symmetrical bond length'
Hf 3   F  -1    2.62     0.37     e   unchecked
Hf 4   O  -2    1.923    0.37     b   ?
Hf 4   O  -2    1.923    0.375    bs  ?
Hf 4   F  -1    1.85     0.37     b   ? 
Hf 4   F  -1    1.82     0.40     p   ? 
Hf 4   Cl -1    2.24     0.37     e   unchecked
Hf 4   Cl -1    2.30     0.37     b   ?
Hf 9   Br -1    2.47     0.37     b   ? 
Hf 9   S  -2    2.39     0.37     b   ? 
Hf 9   Se -2    2.52     0.37     b   ? 
Hf 9   Te -2    2.72     0.37     b   ? 
Hf 9   I  -1    2.68     0.37     b   ? 
Hf 9   N  -3    2.09     0.37     b   ?
Hf 9   P  -3    2.48     0.37     b   ? 
Hf 9   As -3    2.56     0.37     b   ? 
Hf 9   H  -1    1.78     0.37     b   ? 
Hg 1   O  -2    1.90     0.37     b   ? 
Hg 1   F  -1    1.81     0.37     b   ? 
Hg 1   Cl -1    2.28     0.37     b   ?
Hg 2   O  -2    1.924    0.38     bj  ? 
Hg 2   O  -2    1.972    0.37     a   ?
Hg 2   O  -2    1.947    0.370    bs  ?
Hg 2   O  -2    1.93     0.37     b   ? 
Hg 2   S  -2    2.308    0.37     a   ? 
Hg 2   F  -1    2.17     0.37     e   unchecked
Hg 2   F  -1    1.90     0.37     b   ?
Hg 2   Cl -1    2.28     0.37     e   ?
Hg 2   Cl -1    2.25     0.37     b   ? 
Hg 2   Br -1    2.38     0.37     e   unchecked
Hg 2   I  -1    2.62     0.37     e   unchecked
Hg 9   Br -1    2.40     0.37     b   ?
Hg 9   I  -1    2.59     0.37     b   ? 
Hg 9   S  -2    2.32     0.37     b   ? 
Hg 9   Se -2    2.47     0.37     b   ? 
Hg 9   Te -2    2.61     0.37     b   ? 
Hg 9   N  -3    2.02     0.37     b   ? 
Hg 9   P  -3    2.42     0.37     b   ? 
Hg 9   As -3    2.50     0.37     b   ? 
Hg 9   H  -1    1.71     0.37     b   ?
Hg 2   Hg  2    2.51     0.35     f   ?
Ho 3   O  -2    2.025    0.37     a   ?
Ho 3   O  -2    1.993    0.387    bs  ?
Ho 3   O  -2    1.992    0.37     ae  'from transition metal complexes'
Ho 3   S  -2    2.49     0.37     e   unchecked 
Ho 3   F  -1    1.908    0.37     b   ?
Ho 3   F  -1    1.88     0.40     p   ?
Ho 3   Cl -1    2.401    0.37     b   ?
Ho 3   Cl -1    2.37     0.40     p   ?
Ho 3   Cl -1    2.399    0.37     al  ?
Ho 3   Br -1    2.52     0.40     p   ?
Ho 3   I  -1    2.76     0.40     p   ?
Ho 9   Br -1    2.55     0.37     b   ?
Ho 9   I  -1    2.77     0.37     b   ?
Ho 9   S  -2    2.48     0.37     b   ?
Ho 9   Se -2    2.61     0.37     b   ?
Ho 9   Te -2    2.80     0.37     b   ?
Ho 9   N  -3    2.118    0.37     ah  ?
Ho 9   N  -3    2.18     0.37     b   ?
Ho 9   P  -3    2.56     0.37     b   ?
Ho 9   As -3    2.64     0.37     b   ?
Ho 9   H  -1    1.88     0.37     b   ?
I  0   I   0    2.195    0.35     e   unchecked
I  1   F  -1    2.32     0.37     e   unchecked
I  1   Cl -1    2.47     0.37     e   unchecked
I  3   O  -2    2.02     0.37     e   unchecked
I  3   F  -1    1.90     0.37     b   ?
I  3   Cl -1    2.39     0.37     e   unchecked
I  5   O  -2    1.990    0.44     bd  ?
I  5   O  -2    1.992    0.474    bs  ?
I  5   O  -2    1.80     1.00     e   ?   
I  5   O  -2    2.003    0.37     a   ?   
I  5   F  -1    1.84     0.37     e   unchecked
I  5   F  -1    1.90     0.37     b   ?
I  5   Cl -1    2.38     0.37     b   ?
I  7   O  -2    1.93     0.37     b   ?           
I  7   F  -1    1.83     0.37     b   ?
I  7   Cl -1    2.31     0.37     b   ?
In 1   Cl -1    2.56     0.37     e   unchecked
In 3   O  -2    1.902    0.37     a   ?
In 3   O  -2    1.823    0.459    bs  ?
In 3   S  -2    2.370    0.37     a   ? 
In 3   F  -1    1.792    0.37     a   ?
In 3   Cl -1    2.28     0.37     b   ? 
In 3   Br -1    2.51     0.35     e   unchecked
In 3   I  -1    2.63     0.37     e   unchecked
In 3   Co -1    2.593    0.35     e   unchecked
In 3   Mn -2    2.604    0.35     e   unchecked
In 9   Br -1    2.41     0.37     b   ?
In 9   I  -1    2.63     0.37     b   ?
In 9   S  -2    2.36     0.37     b   ?
In 9   Se -2    2.47     0.37     b   ? 
In 9   Te -2    2.69     0.37     b   ?
In 9   N  -3    2.03     0.37     b   ?
In 9   P  -3    2.43     0.37     b   ?
In 9   As -3    2.51     0.37     b   ?
In 9   H  -1    1.72     0.37     b   ?
Ir 4   O  -2    1.909    0.258    bs  ? 
Ir 4   O  -2    1.87     0.37     e   unchecked      
Ir 4   F  -1    1.80     0.37     e   unchecked
Ir 5   O  -2    1.916    0.37     b   ?
Ir 5   O  -2    1.909    0.449    bs  ?
Ir 5   O  -2    2.01     0.37     e   unchecked 
Ir 5   F  -1    1.82     0.37     b   ?
Ir 5   Cl -1    2.30     0.37     b   ? 
Ir 9   S  -2    2.38     0.37     b   ? 
Ir 9   Se -2    2.51     0.37     b   ? 
Ir 9   Te -2    2.71     0.37     b   ?
Ir 9   Br -1    2.45     0.37     b   ? 
Ir 9   I  -1    2.66     0.37     b   ? 
Ir 9   N  -3    2.06     0.37     b   ?
Ir 9   P  -3    2.46     0.37     b   ?
Ir 9   As -3    2.54     0.37     b   ?
Ir 9   H  -1    1.76     0.37     b   ?
K  1   O  -2    2.132    0.37     a   ?
K  1   O  -2    2.047    0.398    bs  ?
K  1   O  -2    2.113    0.37     u   ?
K  1   O  -2    1.9548   0.430    c   '6 A cut-off'
K  1   O  -2    1.84     0.48     o   ?
K  1   S  -2    2.59     0.37     b   ?
K  1   S  -2    2.1516   0.580    c   '7 A cut-off'
K  1   S  -2    2.63     0.37     e   unchecked 
K  1   Se -2    2.72     0.37     b   ?
K  1   Se -2    2.2811   0.612    c   '7 A cut-off'
K  1   Te -2    2.93     0.37     b   ?
K  1   Te -2    2.4102   0.653    c   '7 A cut-off'
K  1   F  -1    1.992    0.37     a   ? 
K  1   F  -1    1.8307   0.429    c   '6 A cut-off'
K  1   Cl -1    2.519    0.37     a   ?
K  1   Cl -1    2.0707   0.559    c   '6 A cut-off'
K  1   Br -1    2.66     0.37     b   ?
K  1   Br -1    2.1529   0.603    c   '7 A cut-off'
K  1   I  -1    2.88     0.37     b   ?
K  1   I  -1    2.2821   0.658    c   '7 A cut-off'
K  1   I  -1    2.92     0.37     e   unchecked
K  1   N  -3    2.26     0.37     b   ?
K  1   N  -3    2.30     0.37     e   unchecked
K  1   P  -3    2.64     0.37     b   ?
K  1   As -3    2.83     0.37     b   ?
K  1   H  -1    2.10     0.37     b   ?
Kr 2   F  -1    1.88     0.37     e   ?
La 3   O  -2    2.086    0.45     bj  ?
La 3   O  -2    2.179    0.359    bs  ?
La 3   O  -2    2.172    0.37     a   ?
La 3   O  -2    2.172    0.33     ac  ?
La 3   O  -2    2.148    0.37     ae  'from transition metal complexes'
La 3   S  -2    2.643    0.37     a   ?
La 3   S  -2    2.632    0.37     al  ?
La 3   Se -2    2.74     0.37     b   ?
La 3   Te -2    2.94     0.37     b   ?
La 3   F  -1    2.02     0.40     p   ?
La 3   F  -1    2.08     0.37     e   unchecked
La 3   Cl -1    2.545    0.37     b   ?
La 3   Cl -1    2.57     0.37     e   unchecked
La 3   Cl -1    2.58     0.40     p   ?
La 3   Br -1    2.72     0.37     b   ?
La 3   Br -1    2.66     0.40     p   ?
La 3   I  -1    2.93     0.37     b   ?
La 3   I  -1    2.88     0.40     p   ?
La 3   N  -3    2.261    0.37     ah  ?
La 3   N  -3    2.34     0.37     b   ?
La 3   P  -3    2.73     0.37     b   ?
La 3   As -3    2.80     0.37     b   ?
La 3   H  -1    2.06     0.37     b   ?
Li 1   O  -2    1.466    0.37     a   ?
Li 1   O  -2    1.062    0.642    bs  ?
Li 1   O  -2    1.1745   0.514    c   '6 A cut-off'
Li 1   O  -2    1.174    0.590    ay  '6.0 A cut-off'
Li 1   O  -2    1.29     0.48     o   ?
Li 1   S  -2    1.94     0.37     b   ?
Li 1   S  -2    1.4607   0.656    c   '6 A cut-off'
Li 1   Se -2    2.09     0.37     b   ?
Li 1   Se -2    1.6272   0.681    c   '7 A cut-off'
Li 1   Te -2    2.30     0.37     b   ?
Li 1   Te -2    1.7340   0.717    c   '7 A cut-off'
Li 1   F  -1    1.360    0.37     a   ? 
Li 1   F  -1    1.0968   0.503    c   '6 A cut-off'
Li 1   Cl -1    1.91     0.37     b   ?
Li 1   Cl -1    1.3873   0.640    c   '6 A cut-off'
Li 1   Cl -1    1.94     0.37     e   unchecked 
Li 1   Br -1    2.02     0.37     b   ?
Li 1   Br -1    1.5150   0.674    c   '7 A cut-off'
Li 1   I  -1    2.22     0.37     b   ? 
Li 1   I  -1    1.6754   0.722    c   '7 A cut-off'
Li 1   N  -3    1.61     0.37     b   ?
Li 1   N  -3    1.15     0.631    ay  '6.5 A cut-off'
Lu 3   O  -2    1.971    0.37     b   ?
Lu 3   O  -2    1.939    0.403    bs  ?
Lu 3   O  -2    1.947    0.37     ae  'from transition metal complex'
Lu 3   S  -2    2.43     0.37     b   ? 
Lu 3   Se -2    2.56     0.37     b   ? 
Lu 3   Te -2    2.75     0.37     b   ?
Lu 3   F  -1    1.876    0.37     b   ?
Lu 3   F  -1    1.84     0.40     p   ?
Lu 3   Cl -1    2.361    0.37     b   ?
Lu 3   Cl -1    2.361    0.37     al  ?
Lu 3   Cl -1    2.33     0.40     p   ?
Lu 3   Br -1    2.50     0.37     b   ?
Lu 3   Br -1    2.48     0.40     p   ?
Lu 3   I  -1    2.73     0.37     b   ?
Lu 3   I  -1    2.73     0.40     p   ?
Lu 3   N  -3    2.046    0.37     ah  ?
Lu 3   N  -3    2.11     0.37     b   ?
Lu 3   P  -3    2.51     0.37     b   ?
Lu 3   As -3    2.59     0.37     b   ?
Lu 3   H  -1    1.82     0.37     b   ?
Mg 2   O  -2    1.693    0.37     a   ? 
Mg 2   O  -2    1.608    0.443    bs  ? 
Mg 2   O  -2    1.636    0.42     o   ? 
Mg 2   S  -2    2.18     0.37     b   ?
Mg 2   Se -2    2.32     0.37     b   ?
Mg 2   Te -2    2.53     0.37     b   ? 
Mg 2   F  -1    1.578    0.37     a   ? 
Mg 2   Cl -1    2.08     0.37     b   ?
Mg 2   Br -1    2.28     0.37     b   ? 
Mg 2   I  -1    2.46     0.37     b   ? 
Mg 2   N  -3    1.85     0.37     b   ?
Mg 2   P  -3    2.29     0.37     b   ?
Mg 2   As -3    2.38     0.37     b   ?
Mg 2   H  -1    1.53     0.37     b   ?
Mn 2   O  -2    1.790    0.37     a   ?
Mn 2   O  -2    1.740    0.417    bs  ?
Mn 2   O  -2    1.765    0.37     j   ?
Mn 2   O  -2    1.762    0.40     ap  'R0 fixed by Mn2O7'
Mn 2   S  -2    2.22     0.37     e   unchecked 
Mn 2   F  -1    1.698    0.37     a   ?
Mn 2   Cl -1    2.133    0.37     a   ?
Mn 2   Br -1    2.34     0.37     e   unchecked
Mn 2   I  -2    2.52     0.37     e   unchecked
Mn 2   N  -3    1.84     0.37     bq  'high spin'
Mn 2   N  -3    1.68     0.37     bq  'intermediate spin'
Mn 2   N  -3    1.53     0.37     bq  'low spin'
Mn 2   N  -3    1.849    0.37     j   'from transition metal complexes'
Mn 3   O  -2    1.760    0.37     a   ?
Mn 3   O  -2    1.823    0.247    bs  ?
Mn 3   O  -2    1.732    0.37     j   'from transition metal complexes'
Mn 3   O  -2    1.762    0.35     ap  'R0 fixed by Mn2O7'
Mn 3   F  -1    1.66     0.37     b   ?
Mn 3   F  -1    1.666    0.36     at  ?
Mn 3   Cl -1    2.14     0.37     b   ?
Mn 3   N  -3    1.82     0.37     bq  'high spin'
Mn 3   N  -3    1.71     0.37     bq  'low spin'
Mn 3   N  -3    1.837    0.37     j   'from transition metal complexes'
Mn 4   O  -2    1.753    0.37     a   ?
Mn 4   O  -2    1.750    0.374    bs  ?
Mn 4   O  -2    1.750    0.37     j   'from transition metal complexes'
Mn 4   O  -2    1.762    0.34     ap  'R0 fixed by Mn2O7 Small sample'
Mn 4   F  -1    1.71     0.37     b   ?           
Mn 4   F  -1    1.63     0.37     e   unchecked
Mn 4   Cl -1    2.13     0.37     b   ?
Mn 4   N  -3    1.822    0.37     j   'from transition metal complexes'
Mn 5   O  -2    1.781    0.375    bs  ?
Mn 5   O  -2    1.762    0.30     ap  'R0 fixed by Mn2O7'
Mn 6   O  -2    1.814    0.375    bs  ?
Mn 6   O  -2    1.79     0.37     e   ?
Mn 6   O  -2    1.762    0.27     ap  'R0 fixed by Mn2O7'
Mn 7   O  -2    1.819    0.375    bs  ?
Mn 7   O  -2    1.827    0.37     e   unchecked
Mn 7   O  -2    1.79     0.37     b   ?
Mn 7   O  -2    1.762    0.26     ap  'R0 fixed by Mn2O7'
Mn 7   F  -1    1.72     0.37     b   ?
Mn 7   Cl -1    2.17     0.37     b   ?
Mn 9   O  -2    1.754    0.37     g   'from transition metal complexes'
Mn 9   Br -1    2.26     0.37     b   ?
Mn 9   I  -1    2.49     0.37     b   ?
Mn 9   S  -2    2.20     0.37     b   ?
Mn 9   Se -1    2.32     0.37     b   ? 
Mn 9   Te -2    2.55     0.37     b   ?
Mn 9   N  -3    1.87     0.37     b   ?
Mn 9   P  -3    2.24     0.37     b   ?
Mn 9   As -3    2.36     0.37     b   ?
Mn 9   H  -1    1.55     0.37     b   ?
Mo 2   S  -2    2.072    0.422    ax  '5.5 A cut-off'
Mo 2   Cl -1    2.052    0.441    ax  '5.5 A cut-off'
Mo 3   O  -2    1.834    0.37     m   ?
Mo 3   O  -2    1.792    0.436    bs  ?
Mo 3   O  -2    1.789    0.418    ax  '5.5 A cut-off'
Mo 3   S  -2    2.062    0.519    ax  '6.0 A cut-off'
Mo 3   F  -1    1.76     0.35     e   unchecked
Mo 3   F  -1    1.738    0.427    ax  '5.5 A cut-off'
Mo 3   Cl -1    2.22     0.37     e   unchecked
Mo 3   Cl -1    2.089    0.501    ax  '6.0 A cut-off'
Mo 3   Br -1    2.34     0.37     e   unchecked
Mo 3   Br -1    2.191    0.541    ax  '6.0 A cut-off'
Mo 3   N  -3    1.96     0.37     e   unchecked
Mo 4   O  -2    1.886    0.37     j   'from transition metal complexes'
Mo 4   O  -2    1.834    0.404    bs  ?
Mo 4   O  -2    1.856    0.37     m   ?
Mo 4   O  -2    1.724    0.562    ax  '6.5 A cut-off'
Mo 4   S  -2    2.235    0.37     j   'from transition metal complexes'
Mo 4   F  -1    1.80     0.37     e   unchecked
Mo 4   Cl -1    2.128    0.558    ax  '6.5 A cut-off'
Mo 4   N  -3    2.043    0.37     j   'from transition metal complexes'
Mo 5   O  -2    1.907    0.37     j   'from transition metal complexes'
Mo 5   O  -2    1.888    0.314    bs  ?
Mo 5   O  -2    1.878    0.37     m   ?
Mo 5   O  -2    1.848    0.482    ax  '5.5 A cut-off'
Mo 5   S  -2    2.288    0.37     j   'from transition metal complexes'
Mo 5   Cl -1    2.26     0.37     e   unchecked
Mo 5   N  -3    2.009    0.37     j   'from transition metal complexes'
Mo 6   O  -2    1.907    0.37     a   ?
Mo 6   O  -2    1.903    0.349    bs  ?
Mo 6   O  -2    1.915    0.41     x   ?
Mo 6   O  -2    1.87     0.26     n   ?
Mo 6   O  -2    1.900    0.37     m   ?
Mo 6   O  -2    1.912    0.405    ax  '5.0 A cut-off'
Mo 6   S  -2    2.331    0.37     j   'from transition metal complexes'
Mo 6   F  -1    1.81     0.37     b   ? 
Mo 6   Cl -1    2.28     0.37     b   ?
Mo 6   N  -3    2.009    0.37     j   'from transition metal complexes'
Mo 9   O  -2    1.879    0.30     z   'applies to all oxidation states'
Mo 9   Br -1    2.43     0.37     b   ? 
Mo 9   I  -1    2.64     0.37     b   ?
Mo 9   S  -2    2.35     0.37     b   ? 
Mo 9   Se -2    2.49     0.37     b   ?
Mo 9   Te -2    2.69     0.37     b   ?
Mo 9   N  -3    2.04     0.37     b   ?
Mo 9   P  -3    2.44     0.37     b   ?
Mo 9   As -3    2.52     0.37     b   ?
Mo 9   H  -1    1.73     0.37     b   ?
N  3   O  -2    1.361    0.37     a   ?
N  3   S  -2    1.73     0.37     e   unchecked      
N  3   F  -1    1.37     0.37     b   ?
N  3   Cl -1    1.75     0.37     b   ?
N -3   N  -3    1.44     0.35     e   unchecked
N  5   O  -2    1.432    0.37     a   ?    
N  5   O  -2    1.492    0.482    bs  ?    
N  5   O  -2    1.41     0.43     o   ?           
N  5   F  -1    1.36     0.37     b   ?
N  5   Cl -1    1.80     0.37     b   ?
Na 1   O  -2    1.803    0.37     a   ?
Na 1   O  -2    1.695    0.420    a   ?
Na 1   O  -2    1.756    0.37     v   ? 
Na 1   O  -2    1.5766   0.475    c   '6 A cut-off'
Na 1   O  -2    1.661    0.44     o   ? 
Na 1   S  -2    2.300    0.37     a   ? 
Na 1   S  -2    2.28     0.37     b   ?
Na 1   S  -2    1.8213   0.626    c   '6 A cut-off'
Na 1   Se -2    2.41     0.37     b   ? 
Na 1   Se -2    1.8908   0.654    c   '7 A cut-off'
Na 1   Te -2    2.64     0.37     b   ?
Na 1   Te -2    2.0400   0.690    c   '7 A cut-off'
Na 1   F  -1    1.677    0.37     a   ?
Na 1   F  -1    1.4485   0.465    c   '6 A cut-off'
Na 1   Cl -1    2.15     0.37     b   ?
Na 1   Cl -1    1.6833   0.608    c   '6 A cut-off'
Na 1   Cl -1    2.22     0.37     e   unchecked 
Na 1   Br -1    2.33     0.37     b   ?
Na 1   Br -1    1.7719   0.646    c   '7 A cut-off'
Na 1   I  -1    2.56     0.37     b   ?
Na 1   I  -1    1.9555   0.695    c   '7 A cut-off'
Na 1   N  -3    1.93     0.37     b   ?
Na 1   N  -3    2.01     0.37     e   unchecked
Na 1   P  -3    2.36     0.37     b   ?
Na 1   As -3    2.53     0.37     b   ?
Na 1   H  -1    1.68     0.37     b   ?
Nb 3   O  -2    1.91     0.35     e   unchecked      
Nb 3   F  -1    1.71     0.37     e   unchecked
Nb 3   Cl -1    2.20     0.37     e   unchecked
Nb 3   Br -1    2.35     0.37     e   unchecked
Nb 4   O  -2    1.853    0.479    bs  ?
Nb 4   O  -2    1.88     0.37     e   unchecked
Nb 4   F  -1    1.90     0.37     e   unchecked
Nb 4   Cl -1    2.26     0.35     e   unchecked 
Nb 4   Cl -1    2.236    0.37     av  'based on eq. 5 in ref. a, small sample'
Nb 4   Br -1    2.62     0.37     e   unchecked
Nb 4   N  -3    2.004    0.37     av  'based on eq. 5 in ref. a, small sample'
Nb 5   O  -2    1.911    0.37     a   ?
Nb 5   O  -2    1.909    0.369    bs  ?
Nb 5   O  -2    1.916    0.37     x   ?
Nb 5   F  -1    1.87     0.37     b   ? 
Nb 5   Cl -1    2.27     0.37     b   ?
Nb 5   I  -1    2.77     0.37     e   unchecked
Nb 5   N  -3    2.01     0.35     e   unchecked
Nb 9   Br -1    2.45     0.37     b   ?
Nb 9   I  -1    2.68     0.37     b   ?
Nb 9   S  -2    2.37     0.37     b   ?
Nb 9   Se -2    2.51     0.37     b   ? 
Nb 9   Te -2    2.70     0.37     b   ?
Nb 9   N  -3    2.06     0.37     b   ?
Nb 9   P  -3    2.46     0.37     b   ?
Nb 9   As -3    2.54     0.37     b   ?
Nb 9   H  -1    1.75     0.37     b   ?
Nd 2   O  -2    1.95     0.37     e   unchecked
Nd 2   S  -2    2.60     0.35     e   unchecked
Nd 3   O  -2    2.021    0.46     bj  ?
Nd 3   O  -2    2.103    0.371    bs  ?
Nd 3   O  -2    2.105    0.37     a   ?
Nd 3   O  -2    2.117    0.37     b   ?
Nd 3   O  -2    2.086    0.37     ae  'from transition metal complexes'
Nd 3   S  -2    2.59     0.37     b   ?
Nd 3   S  -2    2.559    0.37     al  ? 
Nd 3   Se -2    2.71     0.37     b   ?
Nd 3   Te -2    2.89     0.37     b   ?
Nd 3   F  -1    2.008    0.37     b   ? 
Nd 3   F  -1    1.98     0.40     p   ? 
Nd 3   Cl -1    2.492    0.37     b   ?
Nd 3   Cl -1    2.512    0.37     al  ? 
Nd 3   Cl -1    2.46     0.40     p   ? 
Nd 3   Br -1    2.66     0.37     b   ?
Nd 3   Br -1    2.61     0.40     p   ?
Nd 3   I  -1    2.87     0.37     b   ?
Nd 3   I  -1    2.84     0.40     p   ?
Nd 3   N  -3    2.201    0.37     ah  ?
Nd 3   N  -3    2.30     0.37     b   ?
NH 1   O  -2    2.226    0.37     s   ?
NH 1   F  -1    2.129    0.37     s   ?
NH 1   Cl -1    2.619    0.37     s   ?
Ni 2   O  -2    1.675    0.37     e   'better value than ref. a'
Ni 2   O  -2    1.689    0.347    bs  ?
Ni 2   O  -2    1.670    0.37     j   'from transition metal complexes'
Ni 2   O  -2    1.654    0.37     a   ?
Ni 2   S  -2    1.98     0.37     e   unchecked
Ni 2   S  -2    1.937    0.37     j   'from transition metal complexes'
Ni 2   F  -1    1.596    0.37     a   ? 
Ni 2   Cl -1    2.02     0.37     b   ?
Ni 2   Br -1    2.20     0.37     e   unchecked
Ni 2   I  -1    2.40     0.37     e   unchecked
Ni 2   N  -3    1.70     0.37     e   unchecked
Ni 2   N  -3    1.647    0.37     j   'from transition metal complexes'
Ni 3   O  -2    1.75     0.37     e   ?
Ni 3   S  -2    2.040    0.37     j   'from transition metal complexes'
Ni 3   F  -1    1.58     0.37     e   unchecked
Ni 3   N  -3    1.731    0.37     j   'from transition metal complexes'
Ni 4   O  -2    1.734    0.335    bs  ?
Ni 4   F  -1    1.61     0.37     e   unchecked
Ni 9   Br -1    2.16     0.37     b   ?
Ni 9   I  -1    2.34     0.37     b   ?
Ni 9   S  -2    2.04     0.37     b   ?
Ni 9   Se -2    2.14     0.37     b   ? 
Ni 9   Te -2    2.43     0.37     b   ?
Ni 9   N  -3    1.75     0.37     b   ?
Ni 9   P  -3    2.17     0.37     b   ?
Ni 9   As -3    2.24     0.37     b   ?
Ni 9   H  -1    1.40     0.37     b   ?
Np 3   F  -1    2.00     0.40     p   ?
Np 3   Cl -1    2.48     0.40     p   ?
Np 3   Br -1    2.62     0.40     p   ?
Np 3   I  -1    2.85     0.40     p   ?
Np 4   O  -2    2.18     0.37     e   unchecked      
Np 4   O  -2    2.11     0.35     p   ?
Np 4   F  -1    2.02     0.37     e   unchecked
Np 4   F  -1    1.98     0.40     p   ?
Np 4   Cl -1    2.46     0.40     p   ?
Np 5   O  -2    2.036    0.411    bs  ?
Np 5   O  -2    2.09     0.35     p   ?
Np 5   F  -1    1.97     0.40     p   ?
Np 5   Cl -1    2.42     0.40     p   ?
Np 6   O  -2    2.022    0.523    bs  ?
Np 6   O  -2    2.07     0.35     p   ?
Np 6   F  -1    1.97     0.40     p   ?
Np 7   O  -2    2.076    0.477    bs  'sample of two'
Np 7   O  -2    2.06     0.35     p   ?
O -2   O  -2    1.406    0.37     e   unchecked
Os 4   O  -2    1.811    0.37     b   ?
Os 4   S  -2    2.21     0.37     e   unchecked 
Os 4   F  -1    1.72     0.37     b   ?
Os 4   Cl -1    2.19     0.37     b   ?
Os 4   Br -1    2.37     0.37     e   unchecked
Os 5   O  -2    1.870    0.485    bs  'small sample'
Os 5   F  -1    1.81     0.37     e   unchecked
Os 6   O  -2    1.904    0.375    bs  'sample of one'
Os 6   O  -2    2.03     0.37     e   unchecked   
Os 6   F  -1    1.80     0.35     e   unchecked
Os 7   O  -2    1.937    0.349    bs  ?
Os 8   O  -2    1.966    0.405    bs  ?
Os 8   O  -2    1.92     0.37     e   unchecked
P  3   O  -2    1.655    0.399    bs  ?
P  3   O  -2    1.63     0.37     e   unchecked
P  3   S  -2    2.12     0.37     e   unchecked
P  3   Se -2    2.24     0.37     e   unchecked        
P  3   F  -1    1.53     0.35     e   unchecked
P  4   O  -2    1.64     0.37     e   unchecked
P  4   S  -2    2.13     0.35     e   unchecked             
P  4   F  -1    1.66     0.37     e   unchecked
P  5   O  -2    1.617    0.37     a   ?
P  5   O  -2    1.624    0.399    bs  ?
P  5   O  -2    1.615    0.37     au  ?
P  5   O  -2    1.604    0.37     b   ?
P  5   S  -2    2.145    0.37     a   ?
P  5   F  -1    1.54     0.37     e   unchecked
P  5   Cl -1    2.02     0.37     e   ?
P  5   Br -1    2.17     0.40     e   unchecked 
P  5   N  -3    1.704    0.37     a   ?
P  9   Br -1    2.15     0.37     b   ?
P  9   I  -1    2.40     0.37     b   ? 
P  9   S  -2    2.11     0.37     b   ?
P  9   Se -2    2.26     0.37     b   ?
P  9   Te -2    2.44     0.37     b   ?
P  9   N  -3    1.73     0.37     b   ?
P  9   P  -3    2.19     0.37     b   ?
P  9   As -3    2.25     0.37     b   ?
P  9   H  -1    1.41     0.37     b   ?
P  5   P   5    2.22     0.35     e   unchecked
Pa 4   O  -2    2.15     0.35     p   ?
Pa 4   F  -1    2.02     0.40     p   ?
Pa 4   Cl -1    2.49     0.40     p   ?
Pa 4   Br -1    2.66     0.40     p   ?
Pa 5   O  -2    2.09     0.35     e   unchecked
Pa 5   O  -2    2.11     0.35     p   ?
Pa 5   F  -1    2.04     0.37     e   unchecked
Pa 5   F  -1    2.01     0.40     p   ?
Pa 5   Cl -1    2.45     0.40     p   ?
Pa 5   Br -1    2.58     0.40     p   ?
Pb 2   O  -2    1.963    0.49     q   ?
Pb 2   O  -2    2.032    0.442    bs  ?
Pb 2   O  -2    2.112    0.37     a   ?
Pb 2   S  -2    2.42     0.50     e   unchecked
Pb 2   S  -2    2.541    0.37     a   ?
Pb 2   Se -2    2.69     0.37     e   unchecked 
Pb 2   F  -1    2.03     0.37     b   ?
Pb 2   F  -1    2.036    0.382    aq  'R0 from gas phase'
Pb 2   Cl -1    2.53     0.37     b   ?
Pb 2   Cl -1    2.447    0.40     aq  'R0 from gas phase, small sample'
Pb 2   Br -1    2.598    0.40     aq  'R0 from gas phase, small sample'
Pb 2   Br -1    2.68     0.37     e   unchecked
Pb 2   I  -1    2.83     0.37     e   unchecked
Pb 2   I  -1    2.804    0.386    aq  'R0 from gas phase, small sample'
Pb 2   N  -3    2.18     0.40     e   unchecked
Pb 4   O  -2    2.042    0.37     a   ?   
Pb 4   O  -2    2.056    0.280    bs  ?   
Pb 4   F  -1    1.94     0.37     b   ?
Pb 4   Cl -1    2.43     0.37     b   ?
Pb 4   Cl -1    2.36     0.37     e   unchecked  
Pb 4   Br -1    3.04     0.35     e   unchecked
Pb 9   Br -1    2.64     0.37     b   ?
Pb 9   I  -1    2.78     0.37     b   ?
Pb 9   S  -2    2.55     0.37     b   ?
Pb 9   Se -2    2.67     0.37     b   ?
Pb 9   Te -2    2.84     0.37     b   ?
Pb 9   N  -3    2.22     0.37     b   ?
Pb 9   P  -3    2.64     0.37     b   ?
Pb 9   As -3    2.72     0.37     b   ?
Pb 9   H  -1    1.97     0.37     b   ?
Pd 2   O  -2    1.792    0.37     b   ?
Pd 2   O  -2    1.749    0.375    bs  ?
Pd 2   S  -2    2.09     0.37     e   unchecked  
Pd 2   F  -1    1.74     0.37     b   ?
Pd 2   Cl -1    2.05     0.37     b   ?
Pd 2   Br -1    2.20     0.37     e   unchecked
Pd 2   I  -1    2.36     0.37     e   unchecked
Pd 2   N  -3    1.82     0.35     e   unchecked
Pd 2   C  -4    1.73     0.37     e   unchecked
Pd 4   O  -2    1.856    0.352    bs  'Sample of two structures'
Pd 4   S  -2    2.30     0.37     e   unchecked
Pd 4   F  -1    1.66     0.37     e   unchecked
Pd 9   Br -1    2.19     0.37     b   ?
Pd 9   I  -1    2.38     0.37     b   ?
Pd 9   S  -2    2.10     0.37     b   ?
Pd 9   Se -2    2.22     0.37     b   ?
Pd 9   Te -2    2.48     0.37     b   ?
Pd 9   N  -3    1.81     0.37     b   ?
Pd 9   P  -3    2.22     0.37     b   ?
Pd 9   As -3    2.30     0.37     b   ?
Pd 9   H  -1    1.47     0.37     b   ?
Pm 3   F  -1    1.96     0.40     p   ?
Pm 3   Cl -1    2.45     0.40     p   ?
Pm 3   Br -1    2.59     0.40     p   ?
Pm 3   Cl -1    2.82     0.40     p   ?
Po 4   O  -2    2.19     0.37     e   unchecked           
Po 4   F  -1    2.38     0.37     e   unchecked
Pr 3   O  -2    2.138    0.37     a   ?
Pr 3   O  -2    2.071    0.411    bs  ?
Pr 3   O  -2    2.098    0.37     ae  'from transition metal complexes'
Pr 3   S  -2    2.60     0.37     b   ?
Pr 3   S  -2    2.594    0.37     al  ? 
Pr 3   Se -1    2.72     0.37     b   ?
Pr 3   Te -2    2.90     0.37     b   ?
Pr 3   F  -1    2.022    0.37     b   ?
Pr 3   F  -1    1.99     0.40     p   ?
Pr 3   Cl -1    2.50     0.37     b   ?
Pr 3   Cl -1    2.521    0.37     al  ?
Pr 3   Cl -1    2.47     0.40     p   ?
Pr 3   Br -1    2.67     0.37     b   ?
Pr 3   Br -1    2.63     0.40     p   ?
Pr 3   I  -1    2.89     0.37     b   ?
Pr 3   I  -1    2.85     0.40     p   ?
Pr 3   N  -3    2.215    0.37     ah  ?
Pr 3   N  -3    2.30     0.37     b   ?
Pr 3   P  -3    2.68     0.37     b   ?
Pr 3   As -3    2.75     0.37     b   ?
Pr 3   H  -1    2.02     0.37     b   ?
Pt 2   O  -2    1.768    0.37     b   ?
Pt 2   O  -2    1.742    0.375    bs  'small sample'
Pt 2   O  -2    1.80     0.37     e   unchecked
Pt 2   S  -2    2.16     0.37     e   unchecked
Pt 2   F  -1    1.68     0.37     b   ?
Pt 2   Cl -1    2.05     0.37     b   ?
Pt 2   Br -1    2.20     0.37     e   unchecked 
Pt 2   C   2    1.760    0.37     a   ?
Pt 2   N  -3    1.81     0.37     e   unchecked
Pt 3   O  -2    1.856    0.407    bs  ?
Pt 3   O  -2    1.87     0.37     e   unchecked        
Pt 3   Cl -1    2.30     0.37     e   unchecked
Pt 3   Br -1    2.47     0.35     e   unchecked
Pt 4   O  -2    1.879    0.37     a   ?
Pt 4   F  -1    1.759    0.37     b   ?
Pt 4   F  -1    2.19     0.37     e   unchecked
Pt 4   Cl -1    2.17     0.37     b   ?
Pt 4   Cl -1    2.32     0.37     e   unchecked
Pt 4   Br -1    2.6      0.35     e   unchecked
Pt 9   Br -1    2.18     0.37     b   ?
Pt 9   I  -1    2.37     0.37     b   ? 
Pt 9   S  -2    2.08     0.37     b   ?
Pt 9   Se -2    2.19     0.37     b   ?
Pt 9   Te -2    2.45     0.37     b   ?
Pt 9   N  -3    1.77     0.37     b   ?
Pt 9   P  -3    2.19     0.37     b   ?
Pt 9   As -3    2.26     0.37     b   ?
Pt 9   H  -1    1.40     0.37     b   ?
Pu 3   O  -2    2.11     0.37     b   ?
Pu 3   O  -2    2.14     0.35     p   ?
Pu 3   F  -1    2.00     0.37     b   ?
Pu 3   F  -1    1.99     0.40     p   ?
Pu 3   Cl -1    2.48     0.37     b   ?
Pu 3   Cl -1    2.46     0.40     p   ?
Pu 3   Br -1    2.60     0.40     p   ?
Pu 3   I  -1    2.84     0.40     p   ?
Pu 4   O  -2    2.09     0.35     p   ?
Pu 4   O  -2    2.068    0.385    bf  ?
Pu 4   F  -1    1.97     0.40     p   ?
Pu 4   Cl -1    2.44     0.40     p   ?
Pu 5   O  -2    2.11     0.37     e   ?
Pu 5   O  -2    2.08     0.35     p   ?
Pu 5   F  -1    1.96     0.40     p   ?
Pu 6   O  -2    2.06     0.35     p   ?
Pu 6   F  -1    1.96     0.40     p   ?
Pu 7   O  -2    2.05     0.35     p   ?
Rb 1   O  -2    2.263    0.37     a   ?
Rb 1   O  -2    1.993    0.478    bs  ?
Rb 1   O  -2    2.0812   0.415    c   '7 A cut-off'
Rb 1   S  -2    2.70     0.37     b   ?
Rb 1   S  -2    2.2991   0.553    c   '7 A cut-off'
Rb 1   S  -2    2.80     0.37     e   unchecked
Rb 1   Se -2    2.81     0.37     b   ?
Rb 1   Se -2    2.3886   0.587    c   '7 A cut-off'
Rb 1   Te -2    3.00     0.37     b   ?
Rb 1   Te -2    2.4175   0.633    c   '8 A cut-off'
Rb 1   F  -1    2.16     0.37     b   ?
Rb 1   F  -1    1.9718   0.412    c   '6 A cut-off'
Rb 1   F  -1    2.20     0.37     e   unchecked
Rb 1   Cl -1    2.652    0.37     a   ?
Rb 1   Cl -1    2.2653   0.531    c   '7 A cut-off'
Rb 1   Br -1    2.78     0.37     b   ?
Rb 1   Br -1    2.3296   0.578    c   '7 A cut-off'
Rb 1   Br -1    2.86     0.37     e   unchecked
Rb 1   I  -1    3.01     0.37     b   ?
Rb 1   I  -1    2.4509   0.638    c   '7 A cut-off'
Rb 1   I  -1    3.12     0.37     e   unchecked
Rb 1   N  -3    2.62     0.37     e   unchecked
Rb 1   N  -3    2.37     0.37     b   ?
Rb 1   P  -3    2.76     0.37     b   ?
Rb 1   As -3    2.87     0.37     b   ?
Rb 1   H  -1    2.26     0.37     b   ?
Re 1   Cl -1    2.62     0.35     e   unchecked
Re 3   O  -2    1.9      0.35     e   unchecked
Re 3   Cl -1    2.23     0.37     e   unchecked
Re 4   F  -1    1.81     0.37     e   unchecked
Re 4   Cl -1    2.23     0.37     e   unchecked
Re 4   Br -1    2.35     0.37     e   unchecked
Re 5   O  -2    1.834    0.557    bs  'small sample'  
Re 5   O  -2    1.86     0.37     e   ?  
Re 5   Cl -1    2.24     0.37     e   unchecked
Re 6   F  -1    1.79     0.37     e   unchecked
Re 7   O  -2    1.943    0.406    bs  ?
Re 7   O  -2    1.97     0.37     e   unchecked
Re 7   F  -1    1.86     0.37     b   ?  
Re 7   Cl -1    2.23     0.37     b   ? 
Re 9   Br -1    2.45     0.37     b   ? 
Re 9   I  -1    2.61     0.37     b   ?
Re 9   S  -2    2.37     0.37     b   ? 
Re 9   Se -2    2.50     0.37     b   ? 
Re 9   Te -2    2.70     0.37     b   ?
Re 9   N  -3    2.06     0.37     b   ?
Re 9   P  -3    2.46     0.37     b   ?
Re 9   As -3    2.54     0.37     b   ?
Re 9   H  -1    1.75     0.37     b   ?
Rh 3   O  -2    1.793    0.37     b   ?
Rh 3   O  -2    1.769    0.369    bs  ?
Rh 3   F  -1    1.71     0.37     b   ?
Rh 3   Cl -1    2.08     0.37     e   unchecked
Rh 3   Cl -1    2.17     0.37     b   ?
Rh 3   Br -1    2.27     0.35     e   unchecked
Rh 3   N  -3    1.82     0.35     e   unchecked
Rh 4   O  -2    2.836    0.422    bs  ?
Rh 4   F  -1    1.59     0.37     e   unchecked
Rh 5   F  -1    1.80     0.37     e   unchecked
Rh 9   Br -1    2.25     0.37     b   ?
Rh 9   I  -1    2.48     0.37     b   ? 
Rh 9   S  -2    2.15     0.37     b   ?
Rh 9   Se -1    2.33     0.37     b   ? 
Rh 9   Te -2    2.55     0.37     b   ?
Rh 9   N  -3    1.88     0.37     b   ?
Rh 9   P  -3    2.29     0.37     b   ?
Rh 9   As -3    2.37     0.37     b   ?
Rh 9   H  -1    1.55     0.37     b   ?
Ru 2   Se -2    2.11     0.35     e   unchecked      
Ru 2   F  -1    1.84     0.35     e   unchecked
Ru 3   O  -2    1.77     0.37     o   ?
Ru 3   O  -2    1.745    0.401    bs  ?
Ru 3   S  -2    2.20     0.35     e   unchecked      
Ru 3   F  -1    2.12     0.37     e   unchecked
Ru 3   Cl -1    2.25     0.37     e   unchecked
Ru 3   N  -3    1.82     0.35     e   unchecked
Ru 4   O  -2    1.833    0.366    bs  ?
Ru 4   O  -2    1.834    0.37     b   ?
Ru 4   S  -2    2.21     0.37     e   unchecked
Ru 4   F  -1    1.74     0.37     b   ?
Ru 4   Cl -1    2.21     0.37     b   ? 
Ru 5   O  -2    1.90     0.37     o   ?     
Ru 5   O  -2    1.894    0.346    bs  ?     
Ru 5   F  -1    1.82     0.37     e   unchecked
Ru 5   Cl -1    2.23     0.35     e   unchecked
Ru 6   O  -2    1.87     0.35     e   unchecked
Ru 7   O  -2    1.99     0.37     e   unchecked
Ru 9   Br -1    2.26     0.37     b   ?
Ru 9   I  -1    2.48     0.37     b   ? 
Ru 9   S  -2    2.16     0.37     b   ?
Ru 9   Se -2    2.33     0.37     b   ? 
Ru 9   Te -2    2.54     0.37     b   ?
Ru 9   N  -3    1.88     0.37     b   ?
Ru 9   P  -3    2.29     0.37     b   ?
Ru 9   As -3    2.36     0.37     b   ?
Ru 9   H  -1    1.61     0.37     b   ?
S  2   O  -2    1.74     0.37     e   unchecked
S  2   S  -2    2.03     0.37     e   unchecked                  
S  2   N  -2    1.597    0.37     a   ?
S  2   N  -3    1.682    0.37     a   ?
S  2   S   2    2.10     0.35     e   unchecked
S  4   O  -2    1.644    0.37     a   ?
S  4   O  -2    1.643    0.399    bs  ?
S  4   S  -4    2.35     0.37     e   unchecked
S  4   F  -1    1.60     0.37     b   ? 
S  4   Cl -1    2.02     0.37     b   ?           
S  4   N  -3    1.762    0.37     a   ? 
S  6   O  -2    1.624    0.37     a   ?   
S  6   O  -2    1.634    0.399    bs  ?   
S  6   F  -1    1.56     0.37     b   ?
S  6   Cl -1    2.03     0.37     b   ?
S  6   N  -3    1.72     0.37     e   unchecked 
S  9   Br -1    2.17     0.37     b   ?
S  9   I  -1    2.36     0.37     b   ? 
S  9   S  -2    2.07     0.37     b   ? 
S  9   Se -2    2.21     0.37     b   ?
S  9   Te -2    2.45     0.37     b   ?
S  9   N  -3    1.74     0.37     b   ?
S  9   P  -3    2.15     0.37     b   ?
S  9   As -3    2.25     0.37     b   ?
S  9   H  -1    1.38     0.37     b   ?
Sb 3   O  -2    1.885    0.53     bj  ?
Sb 3   O  -2    1.927    0.446    bg  ?
Sb 3   O  -2    1.925    0.455    be  ?
Sb 3   O  -2    1.932    0.435    bs  ?
Sb 3   O  -2    1.924    0.47     bd  ? 
Sb 3   O  -2    1.955    0.37     an  ?
Sb 3   S  -2    2.38     0.50     e   unchecked
Sb 3   S  -2    2.474    0.37     a   ?
Sb 3   Se -2    2.60     0.37     e   unchecked
Sb 3   F  -1    1.883    0.37     a   ?
Sb 3   F  -1    1.90     0.37     b   ?
Sb 3   Cl -1    2.35     0.37     b   ?
Sb 3   Br -1    2.51     0.37     e   unchecked
Sb 3   I  -1    2.76     0.37     e   unchecked
Sb 3   N  -3    2.108    0.37     d   ?
Sb 5   O  -2    1.904    0.430    be  ?
Sb 5   O  -2    1.892    0.475    bs  ?
Sb 5   O  -2    1.912    0.37     an  ?	
Sb 5   O  -2    1.908    0.409    aw  'small sample'
Sb 5   F  -1    1.797    0.37     a   ?
Sb 5   Cl -1    2.30     0.37     b   ?
Sb 5   Br -1    2.48     0.37     e   unchecked 
Sb 5   N  -3    1.99     0.35     e   unchecked
Sb 9   O  -2    1.934    0.37     an  'use for unknown oxidation state'
Sb 9   S  -2    2.45     0.37     b   ?
Sb 9   Se -2    2.57     0.37     b   ?
Sb 9   Te -2    2.78     0.37     b   ?
Sb 9   Br -1    2.50     0.37     b   ?
Sb 9   I  -1    2.72     0.37     b   ?
Sb 9   N  -3    2.12     0.37     b   ?
Sb 9   P  -3    2.52     0.37     b   ?
Sb 9   As -3    2.60     0.37     b   ?
Sb 9   H  -1    2.77     0.37     b   ?
Sc 3   O  -2    1.849    0.37     a   ?
Sc 3   O  -2    1.780    0.452    bs  ?
Sc 3   O  -2    1.877    0.35     o   ?
Sc 3   S  -2    2.321    0.37     a   ?
Sc 3   Se -2    2.44     0.37     b   ?
Sc 3   Te -2    2.64     0.37     b   ?
Sc 3   F  -1    1.76     0.37     b   ?
Sc 3   Cl -1    2.36     0.37     e   unchecked
Sc 3   Cl -1    2.23     0.37     b   ?
Sc 3   Br -1    2.38     0.37     b   ? 
Sc 3   I  -1    2.59     0.37     b   ?
Sc 3   N  -3    1.98     0.37     b   ?
Sc 3   P  -3    2.40     0.37     b   ?
Sc 3   As -3    2.48     0.37     b   ?
Sc 3   H  -1    1.68     0.37     b   ?
Se 2   S  -2    2.21     0.37     e   unchecked
Se 2   Se -2    2.33     0.37     e   unchecked
Se 4   O  -2    1.811    0.37     a   ?
Se 4   O  -2    1.805    0.401    bs  ?
Se 4   F  -1    1.73     0.37     b   ?
Se 4   Cl -1    2.22     0.37     b   ?
Se 4   Br -1    2.43     0.37     e   unchecked
Se 6   O  -2    1.788    0.37     a   ?
Se 6   O  -2    1.797    0.399    bs  ?
Se 6   F  -1    1.69     0.37     b   ? 
Se 6   Cl -1    2.16     0.37     b   ?
Se 6   N  -3    1.90     0.35     e   unchecked
Se 9   Br -1    2.33     0.37     b   ?
Se 9   I  -1    2.54     0.37     b   ? 
Se 9   S  -2    2.25     0.37     b   ? 
Se 9   Se -2    2.36     0.37     b   ? 
Se 9   Te -2    2.55     0.37     b   ?
Se 9   P  -3    2.34     0.37     b   ?
Se 9   As -3    2.42     0.37     b   ?
Se 9   H  -1    1.54     0.37     b   ?
Si 4   O  -2    1.624    0.37     b   ?
Si 4   O  -2    1.622    0.37     au  ?
Si 4   O  -2    1.640    0.37     a   ?
Si 4   O  -2    1.624    0.389    bs  ?
Si 4   S  -2    2.126    0.37     a   ? 
Si 4   Se -2    2.26     0.37     b   ?
Si 4   Te -2    2.49     0.37     b   ? 
Si 4   F  -1    1.58     0.37     b   ? 
Si 4   Cl -1    2.03     0.37     b   ? 
Si 4   Br -1    2.20     0.37     b   ? 
Si 4   I  -1    2.41     0.37     b   ?
Si 4   C  -4    1.883    0.37     a   ?
Si 4   N  -3    1.724    0.37     a   ?
Si 4   N  -3    1.77     0.37     b   ? 
Si 4   P  -3    2.23     0.37     b   ?
Si 4   As -3    2.31     0.37     b   ?
Si 4   H  -1    1.47     0.37     b   ? 
Sm 2   O  -2    2.116    0.37     ai  ?
Sm 2   O  -2    2.126    0.37     al  ?
Sm 2   N  -3    2.267    0.37     al  ?
Sm 3   O  -2    2.088    0.37     b   ?
Sm 3   O  -2    2.049    0.404    bs  ?
Sm 3   O  -2    2.063    0.37     ae  'from transition metal complexes'
Sm 3   O  -2    2.055    0.37     ai  'from transition metal complexes'
Sm 3   S  -2    2.55     0.37     b   ?
Sm 3   S  -2    2.538    0.37     al  ?
Sm 3   Se -2    2.67     0.37     b   ?
Sm 3   Te -2    2.86     0.37     b   ?
Sm 3   F  -1    1.94     0.40     p   ?
Sm 3   F  -1    2.00     0.37     e   unchecked
Sm 3   Cl -1    2.466    0.37     b   ?
Sm 3   Cl -1    2.481    0.37     al  ?
Sm 3   Cl -1    2.43     0.40     p   ?
Sm 3   Br -1    2.66     0.37     b   ?
Sm 3   Br -1    2.58     0.40     p   ?
Sm 3   I  -1    2.84     0.37     b   ?
Sm 3   I  -1    2.80     0.40     p   ?
Sm 3   N  -3    2.171    0.37     ah  ?
Sm 3   N  -3    2.24     0.37     b   ?
Sm 3   P  -3    2.63     0.37     b   ?
Sm 3   As -3    2.70     0.37     b   ?
Sm 3   H  -1    1.96     0.37     b   ?
Sn 2   O  -2    1.849    0.50     bd  ?
Sn 2   O  -2    1.859    0.55     bh  ?
Sn 2   O  -2    1.910    0.451    bs  ?
Sn 2   O  -2    1.984    0.37     b   ?
Sn 2   O  -2    1.956    0.37     bn  'in metal organic complexes'
Sn 2   S  -2    2.35     0.50     e   unchecked
Sn 2   S  -2    2.423    0.37     bn  'in metal organic complexes'
Sn 2   Se -2    2.476    0.37     bn  'in metal organic complexes'
Sn 2   Te -2    2.747    0.37     bn  'in metal organic complexes'
Sn 2   F  -1    1.925    0.37     a   ?
Sn 2   F  -1    1.869    0.37     bn  'in metal organic complexes'
Sn 2   Cl -1    2.335    0.43     bi  'Ro from molecular SnCl2'
Sn 2   Cl -1    2.330    0.37     bn  'in metal organic complexes'
Sn 2   Cl -1    2.36     0.37     b   ?
Sn 2   Br -1    2.500    0.37     bn  'in metal organic complexes'
Sn 2   I  -1    2.752    0.37     bn  'in metal organic complexes'
Sn 2   N  -3    2.046    0.37     bn  'in metal organic complexes'
Sn 2   P  -3    2.488    0.37     bn  'in metal organic complexes'
Sn 2   As -3    2.585    0.37     bn  'in metal organic complexes'
Sn 2   C  -4    2.077    0.37     bn  'in metal organic complexes'
Sn 4   O  -2    1.905    0.37     a   ?
Sn 4   O  -2    1.946    0.274    bs  ?
Sn 4   S  -2    2.399    0.37     a   ?
Sn 4   S  -2    2.393    0.37     bn  'in metal organic complexes'
Sn 4   Se -2    2.524    0.37     bn  'in metal organic complexes'
Sn 4   F  -1    1.843    0.37     a   ?
Sn 4   F  -1    1.802    0.37     bn  'in metal organic complexes'
Sn 4   Cl -1    2.276    0.37     a   ?
Sn 4   Br -1    2.444    0.37     bn  'in metal organic complexes'
Sn 4   I  -1    2.700    0.37     bn  'in metal organic complexes'
Sn 4   N  -3    2.024    0.37     bn  'in metal organic complexes'
Sn 9   Br -1    2.55     0.37     b   ?
Sn 9   I  -1    2.76     0.37     b   ?
Sn 9   S  -2    2.39     0.37     aa  ?
Sn 9   S  -2    2.45     0.37     b   ?
Sn 9   Se -2    2.59     0.37     b   ?
Sn 9   Te -2    2.76     0.37     b   ?
Sn 9   N  -3    2.06     0.37     aa  ?
Sn 9   N  -3    2.14     0.37     b   ?
Sn 9   P  -3    2.45     0.37     b   ?
Sn 9   As -3    2.62     0.37     b   ?
Sn 9   H  -1    1.85     0.37     b   ?
Sr 2   O  -2    2.118    0.37     a   ?
Sr 2   O  -2    1.958    0.479    bs  ?
Sr 2   S  -2    2.59     0.37     b   ?
Sr 2   S  -2    2.65     0.37     e   unchecked 
Sr 2   Se -2    2.72     0.37     b   ?
Sr 2   Te -2    2.87     0.37     b   ?
Sr 2   Te -2    2.06     0.37     e   unchecked
Sr 2   F  -1    2.019    0.37     b   ?
Sr 2   Cl -1    2.51     0.37     b   ?
Sr 2   Br -1    2.68     0.37     b   ?
Sr 2   I  -1    2.88     0.37     b   ?
Sr 2   N  -3    2.23     0.37     b   ?
Sr 2   P  -3    2.67     0.37     b   ?
Sr 2   As -3    2.76     0.37     b   ?
Sr 2   H  -1    2.01     0.37     b   ?
Ta 4   O  -2    2.29     0.37     e   unchecked
Ta 5   O  -2    1.920    0.37     a   ?
Ta 5   O  -2    1.916    0.343    bs  ?
Ta 5   S  -2    2.47     0.37     e   unchecked
Ta 5   F  -1    1.88     0.37     b   ?
Ta 5   Cl -1    2.30     0.37     b   ?
Ta 9   Br -1    2.45     0.37     b   ? 
Ta 9   I  -1    2.66     0.37     b   ? 
Ta 9   S  -2    2.39     0.37     b   ?
Ta 9   Se -2    2.51     0.37     b   ?
Ta 9   Te -2    2.70     0.37     b   ?
Ta 9   N  -3    2.01     0.37     b   ?
Ta 9   P  -3    2.47     0.37     b   ?
Ta 9   As -3    2.55     0.37     b   ?
Ta 9   H  -1    1.76     0.37     b   ?
Tb 3   O  -2    2.032    0.37     a   ?
Tb 3   O  -2    2.049    0.37     b   ?
Tb 3   O  -2    2.020    0.379    bs  ?
Tb 3   O  -2    2.013    0.37     ae  'from transition metal complexes'
Tb 3   S  -2    2.51     0.37     b   ?
Tb 3   S  -2    2.498    0.37     al  ?
Tb 3   Se -2    2.63     0.37     b   ?
Tb 3   Te -2    2.82     0.37     b   ?
Tb 3   F  -1    1.936    0.37     b   ?
Tb 3   F  -1    1.90     0.40     p   ?
Tb 3   Cl -1    2.427    0.37     b   ?
Tb 3   Cl -1    2.437    0.37     al  ?
Tb 3   Cl -1    2.39     0.40     p   ?
Tb 3   Br -1    2.58     0.37     b   ?
Tb 3   Br -1    2.54     0.40     p   ?
Tb 3   I  -1    2.80     0.37     b   ?
Tb 3   I  -1    2.77     0.40     p   ?
Tb 3   N  -3    2.130    0.37     ah  ?
Tb 3   N  -3    2.20     0.37     b   ?
Tb 3   P  -3    2.59     0.37     b   ?
Tb 3   As -3    2.66     0.37     b   ?
Tb 3   H  -1    1.91     0.37     b   ?
Tb 4   O  -2    2.018    0.395    bs  ?
Tc 3   O  -2    1.768    0.37     as  'small sample'
Tc 4   O  -2    1.841    0.37     as  'small sample'
Tc 4   F  -1    1.88     0.40     p   ?
Tc 4   Cl -1    2.21     0.37     e   unchecked
Tc 5   O  -2    1.859    0.37     as  '6-coordination, small sample'
Tc 5   O  -2    1.870    0.37     as  '5-coordination, small sample'
Tc 6   O  -2    1.955    0.37     as  'small sample'
Tc 7   O  -2    1.909    0.37     as  ?
Tc 7   O  -2    1.915    0.375    bs  ?
Te 4   O  -2    1.955    0.44     bd  ?
Te 4   O  -2    1.960    0.389    bs  ?
Te 4   O  -2    1.960    0.41     bk  'cut off 3.5 A'
Te 4   O  -2    1.977    0.37     a   ?
Te 4   S  -2    2.44     0.37     e   unchecked
Te 4   F  -1    1.87     0.37     b   ?
Te 4   Cl -1    2.312    0.56     bk  'cut off 3.5 A'
Te 4   Cl -1    2.37     0.37     b   ?
Te 4   Br -1    2.55     0.37     e   unchecked
Te 4   I  -1    2.782    0.37     bp  ?
Te 6   O  -2    1.917    0.37     a   ?
Te 6   O  -2    1.922    0.387    bs  ?
Te 6   O  -2    1.921    0.56     bk  'cut off 3.5 A'
Te 6   F  -1    1.82     0.37     b   ?
Te 6   Cl -1    2.30     0.37     b   ?
Te 9   Br -1    2.53     0.37     b   ?
Te 9   I  -1    2.76     0.37     b   ?
Te 9   S  -2    2.45     0.37     b   ?
Te 9   Se -2    2.53     0.37     b   ? 
Te 9   Te -2    2.76     0.37     b   ?
Te 9   N  -3    2.12     0.37     b   ?
Te 9   P  -3    2.52     0.37     b   ?
Te 9   As -3    2.60     0.37     b   ?
Te 9   H  -1    1.83     0.37     b   ?
Th 4   O  -2    2.167    0.37     b   ?
Th 4   O  -2    2.117    0.420    bs  ?
Th 4   O  -2    2.18     0.35     p   ?
Th 4   S  -2    2.64     0.37     b   ? 
Th 4   Se -2    2.76     0.37     b   ?
Th 4   Te -2    2.94     0.37     b   ?
Th 4   F  -1    2.068    0.37     a   ?
Th 4   F  -1    2.05     0.40     p   ?
Th 4   Cl -1    2.55     0.37     b   ?
Th 4   Cl -1    2.52     0.40     p   ?
Th 4   Br -1    2.71     0.37     b   ?
Th 4   Br -1    2.68     0.40     p   ?
Th 4   I  -1    2.93     0.37     b   ?
Th 4   I  -1    2.92     0.40     p   ?
Th 4   I  -1    2.96     0.37     e   unchecked
Th 4   N  -3    2.34     0.37     b   ?
Th 4   P  -3    2.73     0.37     b   ?
Th 4   As -3    2.80     0.37     b   ?
Th 4   H  -1    2.07     0.37     b   ?
Ti 2   F  -1    2.15     0.37     e   unchecked
Ti 2   Cl -1    2.31     0.37     e   unchecked
Ti 2   Br -1    2.49     0.37     e   unchecked
Ti 3   O  -2    1.654    0.545    bs  ?
Ti 3   O  -2    1.791    0.37     b   ?
Ti 3   S  -2    2.11     0.37     e   unchecked      
Ti 3   F  -1    1.723    0.37     b   ?
Ti 3   Cl -1    2.22     0.37     e   unchecked
Ti 3   Cl -1    2.17     0.37     b   ?
Ti 3   I  -1    2.52     0.37     e   unchecked
Ti 4   O  -2    1.815    0.37     a   ?
Ti 4   O  -2    1.819    0.342    bs  ?
Ti 4   O  -2    1.78     0.43     o   ?
Ti 4   S  -2    2.29     0.37     e   unchecked
Ti 4   F  -1    1.76     0.37     b   ?
Ti 4   Cl -1    2.19     0.37     b   ?
Ti 4   Br -1    2.36     0.37     e   unchecked
Ti 9   O  -2    1.790    0.37     k   'from transition metal complexes'
Ti 9   Cl -1    2.184    0.37     k   'from transition metal complexes'
Ti 9   Br -1    2.32     0.37     b   ?
Ti 9   I  -1    2.54     0.37     b   ?
Ti 9   S  -2    2.24     0.37     b   ?
Ti 9   Se -2    2.38     0.37     b   ? 
Ti 9   Te -2    2.60     0.37     b   ?
Ti 9   N  -3    1.93     0.37     b   ?
Ti 9   N  -3    1.906    0.37     k   'from transition metal complexes'
Ti 9   P  -3    2.36     0.37     b   ?
Ti 9   As -3    2.42     0.37     b   ?
Ti 9   H  -1    1.61     0.37     b   ?
Tl 1   O  -2    2.124    0.37     a   ?
Tl 1   O  -2    2.063    0.422    bs  ?
Tl 1   O  -2    2.172    0.37     b   ?
Tl 1   O  -2    2.162    0.37     bm  'in metal organic complexes'
Tl 1   O  -2    1.927    0.50     af  'inorganic and organic compounds'
Tl 1   S  -2    2.545    0.37     a   ?
Tl 1   F  -1    2.15     0.37     b   ?
Tl 1   Cl -1    2.56     0.37     b   ?
Tl 1   Cl -1    2.61     0.37     e   unchecked
Tl 1   Br -1    2.69     0.37     e   unchecked
Tl 1   I  -1    2.822    0.37     a   ?
Tl 1   N  -3    2.286    0.37     bm  'in metal organic complexes'
Tl 3   O  -2    2.003    0.37     b   ?
Tl 3   O  -2    1.874    0.504    bs  ?
Tl 3   O  -2    2.162    0.37     bm  'in metal organic complexes'
Tl 3   F  -1    1.88     0.37     b   ?
Tl 3   Cl -1    2.32     0.37     b   ?
Tl 3   Br -1    2.65     0.35     e   unchecked
Tl 3   N  -3    2.014    0.37     bm  'in metal organic complexes'
Tl 9   Br -1    2.70     0.37     b   ?
Tl 9   I  -1    2.91     0.37     b   ?
Tl 9   S  -2    2.63     0.37     b   ?
Tl 9   Se -2    2.70     0.37     b   ?
Tl 9   Te -2    2.93     0.37     b   ?
Tl 9   N  -3    2.29     0.37     b   ?
Tl 9   P  -3    2.71     0.37     b   ?
Tl 9   As -3    2.79     0.37     b   ?
Tl 9   H  -1    2.05     0.37     b   ?
Tm 3   O  -2    2.000    0.37     b   ?
Tm 3   O  -2    1.997    0.381    bs  ?
Tm 3   O  -2    1.968    0.37     ae  'from transition metal complexes'
Tm 3   S  -2    2.45     0.37     b   ?
Tm 3   Se -2    2.58     0.37     b   ?
Tm 3   Te -2    2.77     0.37     b   ?
Tm 3   F  -1    1.842    0.37     b   ?
Tm 3   F  -1    1.86     0.40     p   ?
Tm 3   F  -1    1.91     0.37     e   unchecked
Tm 3   Cl -1    2.38     0.37     b   ?
Tm 3   Cl -1    2.381    0.37     al  ?
Tm 3   Cl -1    2.35     0.40     p   ?
Tm 3   Br -1    2.53     0.37     b   ?
Tm 3   Br -1    2.50     0.40     p   ?
Tm 3   I  -1    2.74     0.37     b   ?
Tm 3   I  -1    2.74     0.40     p   ?
Tm 3   N  -3    2.14     0.37     b   ?
Tm 3   P  -3    2.53     0.37     b   ?
Tm 3   As -3    2.62     0.37     b   ?
Tm 3   H  -1    1.85     0.37     b   ?
U  2   O  -2    2.08     0.37     e   unchecked
U  3   S  -2    2.54     0.37     e   unchecked
U  3   F  -1    2.02     0.40     p   ?
U  3   F  -1    2.09     0.37     e   unchecked
U  3   Cl -1    2.49     0.40     p   ?
U  3   Br -1    2.64     0.40     p   ?
U  3   I  -1    2.87     0.40     p   ?
U  4   O  -2    2.112    0.37     b   ?
U  4   O  -2    2.100    0.373    bs  ?
U  4   O  -2    2.13     0.35     p   ?
U  4   S  -2    2.55     0.37     e   unchecked
U  4   F  -1    2.038    0.37     a   ?
U  4   F  -1    2.034    0.37     b   ?
U  4   F  -1    2.00     0.40     p   ?
U  4   Cl -1    2.47     0.40     p   ?
U  4   Br -1    2.60     0.40     p   ?
U  4   Br -1    2.61     0.37     e   unchecked
U  4   I  -1    2.88     0.37     e   unchecked
U  4   N  -3    2.18     0.37     e   unchecked
U  5   O  -2    2.075    0.37     b   ?
U  5   O  -2    2.009    0.660    bs  'small sample'
U  5   O  -2    2.10     0.35     p   ?
U  5   F  -1    1.966    0.37     b   ? 
U  5   F  -1    1.99     0.40     p   ? 
U  5   Cl -1    2.46     0.37     b   ?
U  5   Cl -1    2.43     0.40     p   ?
U  5   Br -1    2.7      0.35     e   unchecked
U  6   O  -2    2.051    0.519    r   ?
U  6   O  -2    2.046    0.473    bs  ?
U  6   O  -2    2.045    0.519    bo  ?
U  6   O  -2    2.075    0.37     a   ?
U  6   O  -2    2.08     0.35     p   ?
U  6   F  -1    1.98     0.40     p   ?
U  6   Cl -1    2.42     0.40     p   ?     
U  6   N  -3    1.93     0.35     e   unchecked
U  9   Br -1    2.63     0.37     b   ?
U  9   I  -1    2.84     0.37     b   ?
U  9   S  -2    2.56     0.37     b   ?
U  9   Se -2    2.70     0.37     b   ?
U  9   Te -2    2.86     0.37     b   ?
U  9   N  -3    2.24     0.37     b   ?
U  9   P  -3    2.64     0.37     b   ?
U  9   As -3    2.72     0.37     b   ?
U  9   H  -1    1.97     0.37     b   ?
V  1   O  -2    1.88     0.37     e   unchecked                
V  1   Cl -1    2.00     0.35     e   unchecked
V  2   O  -2    1.70     0.37     e   unchecked
V  2   S  -2    2.11     0.37     e   unchecked
V  2   F  -1    2.16     0.37     e   unchecked
V  2   Cl -1    2.44     0.37     e   unchecked
V  3   O  -2    1.743    0.37     a   ?
V  3   O  -2    1.718    0.412    bs  ?
V  3   O  -2    1.749    0.37     j   'from transition metal complexes'
V  3   S  -2    2.17     0.37     e   unchecked
V  3   S  -2    2.185    0.37     j   ?
V  3   F  -1    1.702    0.37     b   ? 
V  3   Cl -1    2.19     0.37     b   ?
V  3   Br -1    2.33     0.35     e   unchecked
V  3   N  -3    1.813    0.37     j   'from transition metal complexes'
V  3   N  -3    1.84     0.35     e   unchecked
V  4   O  -2    1.784    0.37     a   ?
V  4   O  -2    1.776    0.364    bs  ?
V  4   O  -2    1.780    0.37     j   'from transition metal complexes'
V  4   O  -2    1.735    0.37     j   'vanadyl bond only'
V  4   S  -2    2.226    0.37     j   'from transition metal complexes'
V  4   S  -2    2.181    0.37     j   'vanadyl bond only'
V  4   S  -2    2.24     0.37     e   unchecked
V  4   F  -1    1.70     0.37     b   ?
V  4   Cl -1    2.16     0.37     b   ?
V  4   N  -3    1.875    0.37     j   'from transition metal complexes'
V  5   O  -2    1.803    0.37     a   ?
V  5   O  -2    1.799    0.388    bs  ?
V  5   O  -2    1.799    0.37     x   ?
V  5   S  -2    2.25     0.37     e   unchecked
V  5   F  -1    1.70     0.37     e   unchecked
V  5   Cl -1    2.16     0.37     b   ?
V  9   O  -2    1.788    0.32     ag  'all oxidation states'
V  9   O  -2    1.81     0.34     o   ?
V  9   Br -1    2.30     0.37     b   ? 
V  9   I  -1    2.51     0.37     b   ? 
V  9   S  -2    2.23     0.37     b   ?
V  9   Se -2    2.33     0.37     b   ?
V  9   Te -2    2.57     0.37     b   ?
V  9   N  -3    1.86     0.37     b   ?
V  9   P  -3    2.31     0.37     b   ?
V  9   As -3    2.39     0.37     b   ?
V  9   H  -1    1.58     0.37     b   ?
W  4   O  -2    1.851    0.37     aj  ?
W  5   O  -2    1.881    0.37     aj  ?
W  5   O  -2    1.848    0.553    bs  'small sample'
W  6   O  -2    1.917    0.37     a   ?
W  6   O  -2    1.909    0.339    bs  ?
W  6   O  -2    1.916    0.41     x   ?
W  6   O  -2    1.921    0.37     b   ?
W  6   O  -2    1.906    0.37     aj  ?
W  6   F  -1    1.83     0.37     b   ? 
W  6   Cl -1    2.27     0.37     b   ?
W  9   O  -2    1.896    0.28     aj  'fitted to all oxidation states'
W  9   Br -1    2.45     0.37     b   ? 
W  9   I  -1    2.66     0.37     b   ?
W  9   S  -2    2.39     0.37     b   ?
W  9   Se -2    2.51     0.37     b   ? 
W  9   Te -2    2.71     0.37     b   ?
W  9   N  -3    2.06     0.37     b   ?
W  9   P  -3    2.46     0.37     b   ?
W  9   As -3    2.54     0.37     b   ?
W  9   H  -1    1.76     0.37     b   ?
Xe 2   O  -2    2.05     0.35     e   unchecked      
Xe 2   F  -1    2.02     0.37     e   unchecked
Xe 4   F  -1    1.93     0.37     e   unchecked
Xe 6   O  -2    2.00     0.37     e   unchecked
Xe 6   F  -1    1.89     0.37     e   unchecked
Xe 8   O  -2    1.94     0.37     e   unchecked
Y  3   O  -2    2.028    0.35     bj  ?
Y  3   O  -2    1.978    0.407    bs  ?
Y  3   O  -2    2.019    0.37     a   ?
Y  3   O  -2    2.014    0.37     b   ?
Y  3   S  -2    2.48     0.37     b   ?
Y  3   Se -2    2.61     0.37     b   ?
Y  3   Te -2    2.80     0.37     b   ?
Y  3   F  -1    1.904    0.37     b   ?
Y  3   F  -1    1.87     0.37     e   unchecked 
Y  3   Cl -1    2.40     0.37     b   ?
Y  3   Br -1    2.55     0.37     b   ? 
Y  3   I  -1    2.77     0.37     b   ? 
Y  3   N  -3    2.17     0.37     b   ?
Y  3   P  -3    2.57     0.37     b   ?
Y  3   As -3    2.64     0.37     b   ?
Y  3   H  -1    1.86     0.37     b   ?
Yb 2   O  -2    1.989    0.37     al  ?
Yb 2   N  -3    2.092    0.37     al  ?
Yb 3   O  -2    1.965    0.37     a   ?
Yb 3   O  -2    1.969    0.373    bs  ?
Yb 3   O  -2    1.985    0.37     b   ?
Yb 3   O  -2    1.954    0.37     ae  'from transition metal complexes'
Yb 3   S  -2    2.43     0.37     b   ? 
Yb 3   Se -2    2.56     0.37     b   ?
Yb 3   Te -2    2.76     0.37     b   ?
Yb 3   F  -1    1.875    0.37     b   ?
Yb 3   F  -1    1.85     0.40     p   ?
Yb 3   F  -1    1.90     0.37     e   unchecked
Yb 3   Cl -1    2.371    0.37     b   ?
Yb 3   Cl -1    2.376    0.37     al  ?
Yb 3   Cl -1    2.34     0.40     p   ?
Yb 3   Br -1    2.451    0.37     b   ?
Yb 3   Br -1    2.49     0.40     p   ?
Yb 3   I  -1    2.72     0.37     b   ?
Yb 3   I  -1    2.74     0.40     p   ?
Yb 3   N  -3    2.064    0.37     ah  ?
Yb 3   N  -3    2.12     0.37     b   ?
Yb 3   P  -3    2.53     0.37     b   ?
Yb 3   As -3    2.59     0.37     b   ?
Yb 3   H  -1    1.82     0.37     b   ?
Zn 2   O  -2    1.704    0.37     a   ?
Zn 2   O  -2    1.684    0.383    bs  ?
Zn 2   O  -2    1.675    0.39     o   ?
Zn 2   S  -2    2.09     0.37     b   ?
Zn 2   Se -2    2.22     0.37     b   ?
Zn 2   Te -2    2.45     0.37     b   ?
Zn 2   F  -1    1.62     0.37     b   ?
Zn 2   F  -1    1.67     0.37     e   unchecked
Zn 2   Cl -1    2.01     0.37     b   ?
Zn 2   Br -1    2.15     0.37     b   ?
Zn 2   I  -1    2.36     0.37     b   ?
Zn 2   N  -3    1.77     0.37     b   ?
Zn 2   P  -3    2.15     0.37     b   ?
Zn 2   As -3    2.24     0.37     b   ?
Zn 2   H  -1    1.42     0.37     b   ?
Zr 2   O  -2    2.34     0.37     e   unchecked      
Zr 2   F  -1    2.24     0.37     e   unchecked
Zr 2   Cl -1    2.58     0.37     e   unchecked
Zr 4   O  -2    1.928    0.37     a   ?
Zr 4   O  -2    1.913    0.406    bs  ?
Zr 4   O  -2    1.937    0.37     b   ?
Zr 4   S  -2    2.41     0.37     b   ?
Zr 4   Se -2    2.53     0.37     b   ?
Zr 4   Te -2    2.67     0.37     b   ?
Zr 4   F  -1    1.846    0.37     a   ?
Zr 4   F  -1    1.854    0.37     b   ?
Zr 4   Cl -1    2.33     0.37     b   ?
Zr 4   Br -1    2.48     0.37     b   ? 
Zr 4   I  -1    2.69     0.37     b   ?
Zr 4   N  -3    2.11     0.37     b   ?
Zr 4   N  -3    2.15     0.37     e   unchecked
Zr 4   P  -3    2.52     0.37     b   ?
Zr 4   As -3    2.57     0.37     b   ?
Zr 4   H  -1    1.79     0.37     b   ?
"""


_sBVS_anions = ["O-2","F-1","CL-1","BR-1","I-1","S-2","SE-2","TE-2",  
                       "N-3","P-3","AS-3","H-1","O-1","SE-1"]

_sBVS={  'AG+1' : [
        [ 1.78239, 1.58298, 1.98819, 2.03699, 2.08036, 2.11006, 2.17409, 2.34487, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.394,   0.498,   0.429,   0.470,   0.530,   0.365,   0.385,   0.420,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.438,   9.000,   5.667,   5.000,   4.692,   3.308,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.000,   5.000,   5.500,   6.000,   5.000,   5.000,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'AG+2' : [
        [ 1.72209, 1.63780, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.501,   0.509,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   6.812,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'AG+3' : [
        [ 1.84687, 1.71485, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.444,   0.452,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.250,   8.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'AL+3' : [
        [ 1.59901, 1.41970, 1.89795, 2.04045, 2.24648, 2.05965, 2.17392, 2.38658, 1.69564, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.424,   0.519,   0.646,   0.687,   0.747,   0.550,   0.582,   0.632,   0.502,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.327,   0.000,   0.000,   0.000,   0.000,   4.077,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   6.500,   7.000,   7.000,   6.000,   6.500,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'AS+3' : [
        [ 1.76706, 1.68300, 2.06175, 0.00000, 0.00000, 2.20841, 2.34035, 2.48812, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.404,   0.406,   0.522,   0.000,   0.000,   0.540,   0.571,   0.616,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.000,   6.600,   3.000,   0.000,   0.000,   2.960,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.000,   6.000,   0.000,   0.000,   6.000,   6.500,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'AS+5' : [
        [ 1.76689, 1.60379, 0.00000, 0.00000, 0.00000, 2.27986, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.411,   0.503,   0.000,   0.000,   0.000,   0.534,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.029,   6.000,   0.000,   0.000,   0.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   6.000,   0.000,   0.000,   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'AU+1' : [
        [ 1.71819, 0.00000, 0.00000, 0.00000, 0.00000, 2.06404, 2.17613, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.441,   0.000,   0.000,   0.000,   0.000,   0.342,   0.346,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   2.000,   0.000,   0.000,   0.000,   0.000,   2.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   4.500,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'AU+3' : [
        [ 1.81761, 1.69700, 2.14532, 2.27911, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.498,   0.507,   0.421,   0.461,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,  10.375,   4.250,   5.429,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'B+3 ' : [
        [ 1.35761, 1.19909, 1.67500, 1.82100, 2.00700, 1.78195, 1.91870, 2.09820, 1.46869, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.385,   0.542,   0.669,   0.709,   0.770,   0.573,   0.607,   0.659,   0.315,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.417,   0.000,   0.000,   0.000,   0.000,   3.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.500,   5.000,   6.000,   6.500,   7.000,   6.000,   6.000,   6.500,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'BA+2' : [
        [ 2.15998, 2.06475, 2.41041, 2.48600, 2.64950, 2.44239, 2.51975, 2.68807, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.437,   0.428,   0.519,   0.595,   0.655,   0.573,   0.649,   0.649,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [  10.320,   0.000,   0.000,   0.000,   0.000,   8.703,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.500,   7.000,   7.500,   7.000,   7.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'BE+2' : [
        [ 1.20903, 1.14986, 1.52729, 1.65810, 1.80080, 1.57840, 1.70430, 1.84970, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.541,   0.532,   0.659,   0.699,   0.760,   0.677,   0.708,   0.753,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   7.000,   7.000,   6.500,   7.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'BI+3' : [
        [ 2.03677, 1.93046, 2.34105, 2.46708, 2.63989, 2.41824, 2.54545, 2.82304, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.414,   0.423,   0.505,   0.545,   0.605,   0.523,   0.554,   0.599,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.058,   7.400,   6.500,   6.667,   6.000,   7.917,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   7.000,   7.500,   6.500,   7.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'BI+5' : [
        [ 2.04498, 1.86984, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.371,   0.448,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'BR+7' : [
        [ 1.83658, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.423,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'C+2 ' : [
        [ 1.41368, 1.15907, 0.00000, 0.00000, 2.03000, 0.00000, 0.00000, 0.00000, 1.48523, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.415,   0.407,   0.000,   0.000,   0.634,   0.000,   0.000,   0.000,   0.524,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   1.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0]],
        'C+4 ' : [
        [ 1.39826, 1.37249, 0.00000, 0.00000, 2.09679, 1.84354, 0.00000, 0.00000, 1.55787, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.447,   0.547,   0.000,   0.000,   0.775,   0.579,   0.000,   0.000,   0.529,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.000,   8.333,   0.000,   0.000,   0.000,   3.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   6.000,   0.000,   0.000,   7.000,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0]],
        'CA+2' : [
        [ 1.79519, 1.71038, 2.06262, 2.16860, 2.32420, 2.11148, 2.20285, 2.38860, 2.09085, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.476,   0.467,   0.594,   0.634,   0.695,   0.612,   0.643,   0.689,   0.454,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.544,   0.000,   0.000,   0.000,   0.000,   7.250,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   7.000,   7.000,   7.000,   7.000,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'CD+2' : [
        [ 1.83926, 1.73948, 2.06950, 2.16913, 2.32440, 2.12789, 2.16209, 2.36683, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.407,   0.416,   0.512,   0.553,   0.613,   0.531,   0.561,   0.607,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.176,   7.125,   6.000,   5.273,   5.500,   4.783,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   6.000,   7.000,   5.500,   6.500,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'CE+3' : [
        [ 2.03118, 1.92656, 0.00000, 0.00000, 0.00000, 2.50404, 2.52663, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.449,   0.458,   0.000,   0.000,   0.000,   0.489,   0.520,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   9.147,  12.750,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'CE+4' : [
        [ 2.02821, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.443,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.867,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CL+3' : [
        [ 1.72265, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.491,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   2.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CL+5' : [
        [ 1.69552, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.445,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CL+7' : [
        [ 1.67946, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.443,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CO+1' : [
        [ 1.29501, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.621,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   2.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CO+2' : [
        [ 1.59773, 1.51442, 1.93137, 0.00000, 2.19837, 1.99705, 2.10951, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.451,   0.460,   0.468,   0.000,   0.569,   0.487,   0.518,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.506,   6.000,   4.625,   0.000,   4.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   0.000,   6.000,   5.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'CO+3' : [
        [ 1.59234, 1.56345, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.434,   0.443,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CO+4' : [
        [ 1.79444, 1.70035, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.441,   0.441,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CR+2' : [
        [ 1.59356, 1.54102, 2.01499, 2.12678, 2.28404, 1.90930, 0.00000, 2.18257, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.480,   0.489,   0.439,   0.480,   0.540,   0.458,   0.000,   0.534,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.600,   6.778,   6.000,   6.000,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   6.000,   6.500,   5.500,   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0]],
        'CR+3' : [
        [ 1.66198, 1.58975, 2.00510, 2.13165, 0.00000, 2.04397, 2.14649, 2.30242, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.430,   0.438,   0.489,   0.530,   0.000,   0.508,   0.539,   0.584,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   6.500,   0.000,   5.500,   6.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',       0,     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'CR+4' : [
        [ 1.76095, 1.64899, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.409,   0.418,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.429,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CR+5' : [
        [ 1.76781, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.402,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'CR+6' : [
        [ 1.82471, 0.00000, 2.00700, 2.22400, 2.53730, 2.10300, 2.30000, 2.60900, 1.96859, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.476,   0.000,   0.634,   0.674,   0.735,   0.652,   0.683,   0.729,   0.605,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   6.500,   6.500,   7.000,   6.500,   7.000,   8.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'CS+1' : [
        [ 2.25899, 2.15318, 2.46037, 2.50818, 2.71194, 2.52283, 2.64858, 2.78226, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.419,   0.428,   0.500,   0.541,   0.601,   0.519,   0.550,   0.595,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [  11.790,   0.000,   0.000,   0.000,   0.000,   7.585,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.500,   6.000,   6.500,   7.000,   8.000,   6.500,   7.000,   7.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'CU+1' : [
        [ 1.58730, 0.00000, 1.79822, 1.86810, 1.93067, 1.80744, 1.89561, 1.89529, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.341,   0.000,   0.402,   0.442,   0.503,   0.420,   0.451,   0.497,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   2.560,   0.000,   3.929,   3.889,   4.692,   3.308,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   0.000,   5.000,   5.500,   6.000,   5.000,   5.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'CU+2' : [
        [ 1.57422, 1.49530, 1.90175, 0.00000, 0.00000, 1.94997, 2.02888, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.449,   0.457,   0.470,   0.000,   0.000,   0.488,   0.519,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   2.560,   6.135,   5.692,   0.000,   0.000,   3.880,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   5.500,   0.000,   0.000,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'CU+3' : [
        [ 1.70964, 1.54272, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.427,   0.437,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'D+1 ' : [
        [ 0.87141, 0.70779, 1.01040, 1.20000, 1.29000, 1.19164, 1.29750, 1.40390, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.457,   0.558,   0.685,   0.725,   0.786,   0.591,   0.625,   0.678,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   1.923,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   4.500,   5.500,   6.000,   6.500,   5.500,   6.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'DY+3' : [
        [ 1.96029, 1.85000, 2.28810, 0.00000, 0.00000, 2.34124, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.426,   0.435,   0.493,   0.000,   0.000,   0.512,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.828,   0.000,   7.000,   0.000,   0.000,   7.429,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'ER+3' : [
        [ 1.95608, 1.84663, 2.25982, 0.00000, 0.00000, 2.32366, 2.43420, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.412,   0.421,   0.507,   0.000,   0.000,   0.525,   0.556,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.135,   8.125,   6.333,   0.000,   0.000,   6.375,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'EU+2' : [
        [ 1.89158, 1.81420, 2.41447, 2.50011, 2.66292, 2.47173, 0.00000, 0.00000, 2.18740, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.494,   0.503,   0.425,   0.465,   0.525,   0.443,   0.000,   0.000,   0.430,   0.000,   0.000,   0.000,   0.000,   0.000],
        [  10.111,   7.000,   7.000,   7.333,   7.500,   7.579,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   5.500,   5.500,   6.000,   6.500,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0]],
        'EU+3' : [
        [ 2.00469, 1.87763, 2.31998, 0.00000, 0.00000, 2.39179, 0.00000, 0.00000, 2.16270, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.434,   0.443,   0.485,   0.000,   0.000,   0.503,   0.000,   0.000,   0.455,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.743,   8.000,   8.600,   0.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0]],
        'FE+2' : [
        [ 1.57911, 1.50766, 2.00003, 2.09517, 2.25785, 2.01111, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.480,   0.489,   0.439,   0.479,   0.540,   0.457,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.743,   6.077,   6.000,   6.000,   5.000,   5.400,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.000,   5.500,   6.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'FE+3' : [
        [ 1.70840, 1.63674, 1.98266, 2.13627, 2.37658, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.420,   0.411,   0.538,   0.578,   0.523,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.733,   5.992,   5.429,   4.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.000,   6.000,   6.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'FE+4' : [
        [ 1.76559, 1.76220, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.410,   0.417,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'GA+1' : [
        [ 0.00000, 0.00000, 2.32040, 0.00000, 2.38769, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.440,   0.000,   0.541,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   9.000,   0.000,   9.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   6.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'GA+3' : [
        [ 1.71606, 1.56039, 1.97794, 2.11352, 2.31400, 2.12458, 2.24723, 2.44491, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.373,   0.451,   0.578,   0.619,   0.679,   0.483,   0.513,   0.558,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.905,   0.000,   0.000,   0.000,   0.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   6.500,   6.500,   7.000,   6.000,   6.500,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'GD+3' : [
        [ 1.99654, 1.90718, 2.27126, 0.00000, 0.00000, 2.37028, 0.00000, 0.00000, 2.09519, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.415,   0.406,   0.533,   0.000,   0.000,   0.552,   0.000,   0.000,   0.504,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   8.052,   8.333,   7.750,   0.000,   0.000,   7.200,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0]],
        'GE+2' : [
        [ 0.00000, 0.00000, 2.07494, 0.00000, 2.29129, 0.00000, 0.00000, 2.26937, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.490,   0.000,   0.591,   0.000,   0.000,   0.585,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.500,   0.000,   7.000,   0.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',       0,     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0]],
        'GE+4' : [
        [ 1.73939, 1.57864, 2.07619, 0.00000, 0.00000, 2.19183, 2.33264, 2.57461, 1.84758, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.396,   0.484,   0.610,   0.000,   0.000,   0.514,   0.545,   0.593,   0.469,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.305,   6.000,   5.000,   0.000,   0.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   6.000,   0.000,   0.000,   6.000,   6.000,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'H+1 ' : [
        [ 0.87045, 0.70779, 1.01040, 1.20000, 1.29000, 1.19164, 1.29750, 1.40390, 0.91281, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.457,   0.558,   0.685,   0.725,   0.786,   0.591,   0.625,   0.678,   0.540,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   1.923,   2.000,   6.333,   0.000,   0.000,   1.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   4.500,   5.500,   6.000,   6.500,   5.500,   6.000,   6.500,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bw',     'bv',     'bv',     'bv',     'bw',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'HF+4' : [
        [ 1.83361, 1.77520, 2.24440, 0.00000, 2.57677, 2.23550, 2.37893, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.478,   0.469,   0.483,   0.000,   0.584,   0.615,   0.645,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.105,   7.250,   6.000,   0.000,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   5.500,   6.500,   0.000,   7.000,   7.000,   7.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'HG+1' : [
        [ 1.81280, 1.76507, 2.17341, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.465,   0.473,   0.455,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.786,   5.000,   5.333,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'HG+2' : [
        [ 1.81276, 1.73380, 2.17009, 2.25138, 2.38163, 2.20501, 2.25179, 2.37917, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.465,   0.473,   0.455,   0.495,   0.555,   0.473,   0.504,   0.549,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.966,   6.286,   6.857,   5.167,   4.000,   5.222,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   6.000,   6.000,   5.500,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'HO+3' : [
        [ 1.97099, 1.84485, 0.00000, 0.00000, 0.00000, 2.33798, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.415,   0.424,   0.000,   0.000,   0.000,   0.522,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.500,   8.333,   0.000,   0.000,   0.000,   6.875,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'HX+1' : [
        [ 0.78150, 0.66653, 0.96000, 1.15000, 1.24000, 1.09778, 1.21280, 1.31710, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.457,   0.558,   0.685,   0.725,   0.786,   0.591,   0.625,   0.678,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   1.923,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   4.500,   5.500,   6.000,   6.500,   5.500,   6.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'I+5 ' : [
        [ 1.97775, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.424,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.100,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'I+7 ' : [
        [ 1.92274, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.419,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.800,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'IN+1' : [
        [ 0.00000, 0.00000, 2.43863, 2.46665, 2.50769, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.413,   0.454,   0.514,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   9.000,   8.700,   7.833,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   6.000,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'IN+3' : [
        [ 1.90305, 1.75728, 2.13474, 2.28936, 2.47773, 2.30797, 2.43051, 2.62278, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.353,   0.421,   0.548,   0.589,   0.667,   0.456,   0.484,   0.534,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.024,   6.941,   6.000,   4.400,   4.000,   5.453,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   6.500,   6.500,   7.000,   6.000,   6.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'IR+3' : [
        [ 0.00000, 0.00000, 2.05823, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.402,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'IR+4' : [
        [ 1.83233, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.436,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'IR+5' : [
        [ 1.89791, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.479,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'K+1 ' : [
        [ 1.94117, 1.83331, 2.07673, 2.17206, 2.28880, 2.16803, 2.29712, 2.41802, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.436,   0.428,   0.555,   0.595,   0.655,   0.573,   0.604,   0.649,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   8.846,   0.000,   0.000,   0.000,   0.000,   8.400,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   5.500,   6.500,   7.000,   7.000,   6.500,   7.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'LA+3' : [
        [ 2.06392, 1.96577, 2.43099, 0.00000, 0.00000, 2.40330, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.451,   0.443,   0.459,   0.000,   0.000,   0.588,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   9.830,  10.286,   9.000,   0.000,   0.000,   7.944,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'LI+1' : [
        [ 1.17096, 1.08674, 1.39892, 1.51288, 1.64829, 1.46652, 1.62021, 1.71028, 1.15430, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.516,   0.508,   0.634,   0.675,   0.735,   0.653,   0.684,   0.729,   0.637,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.021,   5.538,   5.867,   5.846,   5.818,   4.385,   4.400,   4.670,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   7.000,   7.000,   6.000,   7.000,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'LU+3' : [
        [ 1.91728, 1.80738, 2.28400, 0.00000, 0.00000, 2.28119, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.421,   0.412,   0.433,   0.000,   0.000,   0.557,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.830,   7.500,   6.000,   0.000,   0.000,   6.077,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'MG+2' : [
        [ 1.48398, 1.40956, 1.78276, 1.89059, 2.04500, 1.82372, 1.70430, 1.94970, 1.63729, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.512,   0.504,   0.630,   0.671,   0.731,   0.649,   0.708,   0.680,   0.601,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.897,   0.000,   0.000,   0.000,   0.000,   5.556,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   7.000,   7.000,   6.500,   7.000,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'MN+2' : [
        [ 1.62758, 1.56491, 1.99681, 2.08701, 2.26045, 2.15468, 2.24751, 2.43113, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.481,   0.474,   0.488,   0.528,   0.588,   0.406,   0.431,   0.470,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.910,   6.242,   5.905,   5.750,   6.000,   5.308,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   6.000,   6.500,   5.500,   5.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'MN+3' : [
        [ 1.68993, 1.59633, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.437,   0.446,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.862,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'MN+4' : [
        [ 1.73272, 1.61606, 2.06541, 0.00000, 0.00000, 2.30057, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.402,   0.410,   0.517,   0.000,   0.000,   0.536,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.923,   6.000,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.000,   6.500,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'MN+5' : [
        [ 1.78879, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.413,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'MN+6' : [
        [ 1.82018, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.416,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'MN+7' : [
        [ 1.87362, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.520,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'MO+2' : [
        [ 0.00000, 0.00000, 2.05175, 2.22218, 2.35705, 2.07169, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.441,   0.401,   0.461,   0.422,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.000,   5.000,   5.000,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.500,   5.500,   6.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bw',     'bv',     'bv',     'bw',       0,       0,       0,       0,       0,       0,       0,       0]],
        'MO+3' : [
        [ 1.78933, 1.73819, 2.08941, 2.19147, 0.00000, 2.06172, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.418,   0.427,   0.501,   0.541,   0.000,   0.519,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.700,   6.000,   6.286,   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bw',     'bw',     'bw',       0,     'bw',       0,       0,       0,       0,       0,       0,       0,       0]],
        'MO+4' : [
        [ 1.72390, 0.00000, 2.12830, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.562,   0.000,   0.558,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.500,   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bw',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'MO+5' : [
        [ 1.84760, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.482,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.980,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'MO+6' : [
        [ 1.90934, 0.00000, 2.08880, 2.30370, 2.61910, 2.18700, 2.38240, 2.66000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.391,   0.000,   0.622,   0.663,   0.723,   0.641,   0.672,   0.717,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.764,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   0.000,   6.500,   6.500,   7.000,   6.500,   6.500,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'N+3 ' : [
        [ 1.40795, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.448,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   2.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'N+5 ' : [
        [ 1.46267, 1.40717, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.450,   0.550,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'NA+1' : [
        [ 1.56225, 1.42885, 1.69489, 1.78228, 1.94353, 1.83088, 1.89880, 2.03011, 1.60725, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.482,   0.474,   0.601,   0.641,   0.701,   0.619,   0.650,   0.695,   0.571,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.520,   0.000,   0.000,   0.000,   0.000,   5.772,   5.210,   5.520,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   5.500,   6.500,   7.000,   7.000,   6.500,   7.000,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'NB+2' : [
        [ 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 2.39087, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.448,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,       0,       0,       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0]],
        'NB+3' : [
        [ 1.74581, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.501,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'NB+4' : [
        [ 1.78543, 1.75844, 0.00000, 0.00000, 0.00000, 2.28012, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.526,   0.534,   0.000,   0.000,   0.000,   0.412,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   0.000,   0.000,   0.000,   5.750,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   0.000,   0.000,   0.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'NB+5' : [
        [ 1.86588, 1.76034, 2.20986, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 2.02880, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.498,   0.489,   0.616,   0.000,   0.000,   0.000,   0.000,   0.000,   0.480,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.044,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,       0,       0,       0,     'bv',       0,       0,       0,       0,       0]],
        'ND+3' : [
        [ 2.02425, 1.91099, 0.00000, 0.00000, 0.00000, 2.44624, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.428,   0.437,   0.000,   0.000,   0.000,   0.510,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   8.647,  10.000,   0.000,   0.000,   0.000,   7.700,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'NH+1' : [
        [ 2.03380, 1.97933, 2.15362, 2.23280, 2.40576, 2.24264, 2.34800, 2.48100, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.442,   0.434,   0.561,   0.601,   0.661,   0.579,   0.610,   0.655,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.467,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   5.500,   6.500,   6.500,   7.000,   7.000,   7.000,   7.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'NI+2' : [
        [ 1.55920, 1.49655, 1.87666, 1.96729, 0.00000, 1.85695, 1.89863, 2.11175, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.443,   0.452,   0.476,   0.516,   0.000,   0.494,   0.525,   0.571,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.933,   6.000,   6.000,   6.000,   0.000,   4.700,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.000,   5.500,   6.000,   0.000,   5.500,   6.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',       0,     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'NI+3' : [
        [ 1.64888, 1.56869, 0.00000, 0.00000, 0.00000, 1.95763, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.414,   0.423,   0.000,   0.000,   0.000,   0.523,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.000,   0.000,   0.000,   0.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'NI+4' : [
        [ 1.72159, 1.61746, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.402,   0.411,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'OS+4' : [
        [ 1.75302, 0.00000, 2.15572, 2.30615, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.498,   0.000,   0.421,   0.461,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'OS+5' : [
        [ 0.00000, 1.75815, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.488,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'OS+6' : [
        [ 1.93192, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.463,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'OS+7' : [
        [ 1.95775, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.479,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'OS+8' : [
        [ 1.97728, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.512,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.333,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'P+3 ' : [
        [ 1.51555, 0.00000, 0.00000, 0.00000, 0.00000, 1.96089, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.402,   0.000,   0.000,   0.000,   0.000,   0.536,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.000,   0.000,   0.000,   0.000,   0.000,   3.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.500,   0.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'P+5 ' : [
        [ 1.62038, 1.47610, 2.01093, 2.21050, 2.49792, 2.14917, 2.43695, 0.00000, 1.73267, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.437,   0.535,   0.662,   0.703,   0.763,   0.566,   0.600,   0.000,   0.517,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   6.000,   4.000,   0.000,   4.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   7.000,   7.000,   7.000,   7.500,   6.000,   7.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,     'bv',       0,       0,       0,       0,       0]],
        'PB+2' : [
        [ 2.01825, 1.90916, 2.34641, 2.43160, 2.56880, 2.38758, 2.46755, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.433,   0.453,   0.474,   0.515,   0.575,   0.493,   0.524,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.541,  10.588,   7.833,   7.714,   6.429,   7.551,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   6.000,   5.500,   6.000,   7.000,   6.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'PB+4' : [
        [ 2.03293, 1.93428, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.354,   0.424,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.740,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'PD+2' : [
        [ 1.62359, 1.56885, 1.99818, 2.10183, 0.00000, 2.02559, 2.13063, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.498,   0.506,   0.421,   0.462,   0.000,   0.439,   0.471,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   6.897,   5.250,   4.667,   0.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.000,   5.500,   0.000,   5.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'PD+4' : [
        [ 1.80500, 1.68582, 2.12662, 0.00000, 0.00000, 0.00000, 2.31115, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.449,   0.457,   0.470,   0.000,   0.000,   0.000,   0.520,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.333,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'PR+3' : [
        [ 2.03652, 1.91752, 2.48619, 0.00000, 0.00000, 2.46496, 2.52676, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.439,   0.448,   0.387,   0.000,   0.000,   0.499,   0.529,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   9.067,   9.000,   8.000,   0.000,   0.000,   8.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   0.000,   0.000,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'PT+2' : [
        [ 1.51205, 0.00000, 1.97699, 0.00000, 0.00000, 2.02450, 2.16525, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.574,   0.000,   0.456,   0.000,   0.000,   0.438,   0.407,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   4.600,   0.000,   0.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   5.500,   0.000,   0.000,   5.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bv',       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'PT+3' : [
        [ 1.66559, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.546,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'PT+4' : [
        [ 1.82198, 1.69132, 2.14110, 0.00000, 0.00000, 2.19999, 2.30943, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.479,   0.488,   0.440,   0.000,   0.000,   0.458,   0.489,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'PT+5' : [
        [ 0.00000, 1.78573, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.424,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RB+1' : [
        [ 2.08597, 1.99137, 2.26585, 2.34362, 2.46445, 2.30817, 2.40364, 2.43463, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.413,   0.404,   0.531,   0.572,   0.632,   0.550,   0.580,   0.626,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [  10.020,   0.000,   0.000,   0.000,   0.000,   6.552,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.500,   5.500,   6.500,   7.000,   7.000,   6.500,   7.000,   7.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'RE+3' : [
        [ 0.00000, 0.00000, 2.15781, 2.30419, 0.00000, 2.20710, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.420,   0.422,   0.000,   0.401,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   9.000,   4.750,   0.000,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.500,   5.500,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'RE+4' : [
        [ 1.78237, 0.00000, 2.18513, 0.00000, 0.00000, 2.26800, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.507,   0.000,   0.412,   0.000,   0.000,   0.431,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   6.000,   0.000,   0.000,   5.400,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   5.500,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'RE+5' : [
        [ 1.82664, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.479,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RE+6' : [
        [ 1.91007, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.498,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RE+7' : [
        [ 1.97792, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.508,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.098,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RH+3' : [
        [ 1.67013, 1.63692, 2.03722, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.478,   0.488,   0.440,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RH+4' : [
        [ 1.77675, 1.68686, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.403,   0.406,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RU+3' : [
        [ 1.72066, 0.00000, 1.99520, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.430,   0.000,   0.489,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RU+4' : [
        [ 1.79363, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.449,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RU+5' : [
        [ 1.87442, 1.77634, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.436,   0.445,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'RU+6' : [
        [ 1.92579, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.425,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'S+4 ' : [
        [ 1.64282, 0.00000, 2.05269, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.427,   0.000,   0.545,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'S+6 ' : [
        [ 1.64220, 1.55000, 0.00000, 0.00000, 0.00000, 2.20000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.441,   0.441,   0.000,   0.000,   0.000,   0.571,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.000,   0.000,   0.000,   0.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'SB+3' : [
        [ 1.92036, 1.83448, 2.30831, 2.38165, 2.59905, 2.36947, 2.47586, 2.73139, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.423,   0.431,   0.496,   0.537,   0.597,   0.515,   0.546,   0.591,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   7.000,   6.400,   7.500,   6.200,   4.337,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   6.000,   7.000,   7.500,   6.000,   6.500,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'SB+5' : [
        [ 1.89768, 1.76603, 2.22320, 0.00000, 0.00000, 2.44254, 2.58978, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.400,   0.489,   0.616,   0.000,   0.000,   0.520,   0.551,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   0.000,   0.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   6.000,   6.500,   0.000,   0.000,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',     'bv',       0,       0,     'bu',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'SC+3' : [
        [ 1.73220, 1.65325, 2.11330, 0.00000, 0.00000, 2.09450, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.494,   0.485,   0.612,   0.000,   0.000,   0.631,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.255,   6.250,   6.000,   0.000,   0.000,   6.048,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   6.000,   6.500,   0.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'SE+4' : [
        [ 1.80095, 0.00000, 2.15849, 2.32723, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.427,   0.000,   0.545,   0.585,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.000,   0.000,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   6.500,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'SE+6' : [
        [ 1.79866, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.416,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'SI+4' : [
        [ 1.60817, 1.45654, 0.00000, 0.00000, 0.00000, 2.09975, 2.23551, 0.00000, 1.69319, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.432,   0.529,   0.000,   0.000,   0.000,   0.560,   0.529,   0.000,   0.511,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.100,   0.000,   0.000,   0.000,   0.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   0.000,   0.000,   0.000,   6.500,   5.500,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',       0,       0,       0,     'bv',     'bv',       0,     'bv',       0,       0,       0,       0,       0]],
        'SM+3' : [
        [ 2.01168, 1.88844, 0.00000, 0.00000, 0.00000, 2.41460, 0.00000, 2.71979, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.433,   0.441,   0.000,   0.000,   0.000,   0.505,   0.000,   0.581,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   8.119,   8.429,   0.000,   0.000,   0.000,   7.667,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   6.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0]],
        'SN+2' : [
        [ 1.87499, 1.80141, 2.28757, 2.37369, 2.54376, 2.32497, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.458,   0.467,   0.461,   0.501,   0.562,   0.479,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.325,   0.000,   0.000,   0.000,   0.000,   4.600,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   6.000,   5.500,   6.000,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'SN+4' : [
        [ 1.89019, 1.75558, 2.17643, 0.00000, 0.00000, 2.36256, 2.50725, 2.73112, 1.99361, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.379,   0.461,   0.588,   0.000,   0.000,   0.492,   0.522,   0.568,   0.449,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.069,   6.000,   5.889,   0.000,   0.000,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   6.500,   0.000,   0.000,   6.000,   6.000,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'SR+2' : [
        [ 1.95311, 1.86817, 2.20197, 2.31250, 2.32420, 2.26765, 2.36718, 2.54050, 2.09477, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.455,   0.446,   0.573,   0.614,   0.695,   0.591,   0.622,   0.668,   0.544,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   9.400,   0.000,   0.000,   0.000,   0.000,   8.074,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   7.000,   7.000,   7.000,   7.000,   7.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'TA+2' : [
        [ 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 2.20689, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.593,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,       0,       0,       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0]],
        'TA+3' : [
        [ 0.00000, 1.52314, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 1.76100, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.555,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.457,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,     'bv',       0,       0,       0,       0,       0,       0,     'bv',       0,       0,       0,       0,       0]],
        'TA+4' : [
        [ 1.75632, 0.00000, 0.00000, 0.00000, 0.00000, 2.28935, 2.36128, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.546,   0.000,   0.000,   0.000,   0.000,   0.410,   0.422,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   5.667,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   5.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'TA+5' : [
        [ 1.86816, 1.79011, 2.21442, 0.00000, 0.00000, 2.27860, 2.51263, 2.71824, 2.00405, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.486,   0.477,   0.604,   0.000,   0.000,   0.622,   0.654,   0.699,   0.463,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.090,   6.400,   6.000,   0.000,   0.000,   7.167,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   0.000,   0.000,   6.500,   7.000,   7.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0]],
        'TB+3' : [
        [ 1.95675, 1.83798, 2.29526, 0.00000, 0.00000, 2.36384, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.433,   0.442,   0.486,   0.000,   0.000,   0.505,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.958,   9.333,   9.000,   0.000,   0.000,   7.600,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'TB+4' : [
        [ 1.96244, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.494,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'TC+4' : [
        [ 0.00000, 0.00000, 2.15861, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.470,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'TC+7' : [
        [ 1.97036, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.514,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'TE+2' : [
        [ 1.39168, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.612,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   2.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'TE+4' : [
        [ 1.95290, 0.00000, 2.30563, 2.46108, 2.67663, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.401,   0.000,   0.518,   0.559,   0.619,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   3.396,   0.000,   6.300,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   6.500,   7.000,   7.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'TE+6' : [
        [ 1.91343, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.412,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'TH+4' : [
        [ 2.04983, 2.40121, 0.00000, 0.00000, 0.00000, 2.45709, 2.54850, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.486,   0.561,   0.000,   0.000,   0.000,   0.579,   0.611,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   8.941,   0.000,   0.000,   0.000,   0.000,   8.667,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   7.000,   0.000,   0.000,   0.000,   7.000,   7.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'TI+2' : [
        [ 0.00000, 0.00000, 2.03427, 2.15487, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.429,   0.470,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.667,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'TI+3' : [
        [ 1.69766, 1.63180, 2.13089, 0.00000, 0.00000, 2.11813, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.460,   0.468,   0.459,   0.000,   0.000,   0.478,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'TI+4' : [
        [ 1.72394, 1.66170, 2.12577, 0.00000, 0.00000, 2.17452, 0.00000, 2.41793, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.503,   0.449,   0.507,   0.000,   0.000,   0.640,   0.000,   0.716,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   0.000,   0.000,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.000,   0.000,   0.000,   7.000,   0.000,   7.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0]],
        'TL+1' : [
        [ 1.91752, 1.82737, 2.36792, 2.42772, 2.48689, 2.38260, 2.39935, 2.50518, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.483,   0.491,   0.491,   0.477,   0.537,   0.455,   0.508,   0.531,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   8.030,  12.625,   8.875,   8.400,   8.200,   7.341,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   6.000,   7.000,   6.000,   6.500,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'TL+3' : [
        [ 2.06297, 1.85700, 2.22567, 2.35992, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.338,   0.325,   0.514,   0.555,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.220,   7.250,   6.222,   4.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.500,   6.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'TM+3' : [
        [ 1.94901, 1.81795, 0.00000, 0.00000, 0.00000, 2.31070, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.421,   0.430,   0.000,   0.000,   0.000,   0.516,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.912,   8.000,   0.000,   0.000,   0.000,   6.312,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'U+6 ' : [
        [ 2.02317, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.527,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.987,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'V+2 ' : [
        [ 1.59976, 1.53303, 2.03267, 2.10218, 0.00000, 1.89815, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.477,   0.485,   0.442,   0.483,   0.000,   0.461,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',     'bv',     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'V+3 ' : [
        [ 1.67799, 1.61581, 2.06334, 0.00000, 0.00000, 2.02622, 2.13686, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.439,   0.448,   0.480,   0.000,   0.000,   0.499,   0.530,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   6.000,   6.000,   0.000,   0.000,   5.920,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   5.500,   0.000,   0.000,   6.500,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'V+4 ' : [
        [ 1.74932, 1.65629, 0.00000, 0.00000, 0.00000, 2.16760, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.426,   0.430,   0.000,   0.000,   0.000,   0.512,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.738,   6.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.000,   0.000,   0.000,   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',     'bv',       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'V+5 ' : [
        [ 1.79445, 0.00000, 0.00000, 0.00000, 0.00000, 2.29252, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.510,   0.000,   0.000,   0.000,   0.000,   0.647,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.166,   0.000,   0.000,   0.000,   0.000,   4.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   0.000,   0.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'W+2 ' : [
        [ 0.00000, 0.00000, 0.00000, 1.95717, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.000,   0.647,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'W+3 ' : [
        [ 0.00000, 0.00000, 2.12237, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.428,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.667,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'W+4 ' : [
        [ 1.74558, 0.00000, 0.00000, 2.35170, 0.00000, 2.22672, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.520,   0.000,   0.000,   0.439,   0.000,   0.417,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   0.000,   6.500,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,       0,     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'W+5 ' : [
        [ 1.81975, 0.00000, 2.24489, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.498,   0.000,   0.420,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'W+6 ' : [
        [ 1.90641, 0.00000, 2.21497, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.401,   0.000,   0.617,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.688,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'XE+2' : [
        [ 0.00000, 1.77407, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.569,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   2.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'XE+4' : [
        [ 0.00000, 1.85567, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.529,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   5.286,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   6.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'XE+6' : [
        [ 0.00000, 1.86157, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.431,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   8.231,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'Y+3 ' : [
        [ 1.90384, 1.89262, 2.28867, 2.40922, 0.00000, 2.25923, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.478,   0.379,   0.483,   0.522,   0.000,   0.615,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   7.285,   7.824,   6.400,   6.000,   0.000,   6.417,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   6.500,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]],
        'YB+2' : [
        [ 1.63254, 0.00000, 2.29464, 0.00000, 0.00000, 2.40079, 2.62618, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.510,   0.000,   0.409,   0.000,   0.000,   0.427,   0.458,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   8.000,   0.000,   6.500,   0.000,   0.000,   7.750,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   0.000,   5.500,   0.000,   0.000,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bv',       0,     'bv',       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'YB+3' : [
        [ 1.92872, 1.80974, 0.00000, 0.00000, 0.00000, 2.31245, 2.42113, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.426,   0.435,   0.000,   0.000,   0.000,   0.511,   0.542,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.875,   7.500,   0.000,   0.000,   0.000,   6.125,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   0.000,   0.000,   0.000,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',       0,       0,       0,     'bv',     'bv',       0,       0,       0,       0,       0,       0,       0]],
        'ZN+2' : [
        [ 1.65344, 1.57447, 1.88195, 1.98741, 2.15151, 1.94373, 2.00075, 2.15126, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.403,   0.406,   0.521,   0.562,   0.622,   0.540,   0.571,   0.616,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   4.718,   6.269,   4.000,   4.000,   4.500,   4.481,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.000,   5.000,   6.000,   6.000,   6.500,   6.000,   6.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',     'bv',       0,       0,       0,       0,       0,       0]],
        'ZR+2' : [
        [ 0.00000, 0.00000, 2.12072, 0.00000, 2.49296, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.478,   0.000,   0.424,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   5.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   6.000,   0.000,   5.500,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'ZR+3' : [
        [ 0.00000, 0.00000, 0.00000, 0.00000, 2.56625, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.000,   0.000,   0.000,   0.000,   0.472,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   0.000,   0.000,   0.000,   0.000,   6.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [       0,       0,       0,       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0,       0]],
        'ZR+4' : [
        [ 1.84505, 1.83174, 2.18437, 2.32815, 0.00000, 2.26265, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
        [   0.490,   0.388,   0.608,   0.648,   0.000,   0.626,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   6.765,   7.146,   6.000,   6.000,   0.000,   6.333,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [   5.500,   5.500,   6.500,   7.000,   0.000,   7.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000,   0.000],
        [     'bu',     'bv',     'bv',     'bv',       0,     'bv',       0,       0,       0,       0,       0,       0,       0,       0]]
  }

  
  

  
import math
#####################################################3
_valence_param_=[line for line in _valence_param_.split("\n") if line.strip()]
lines =[line.strip().split(None,7) for line in _valence_param_]
lines =[line.strip().split(None,7) for line in _valence_param_]
######################################################

######################################################
def _name1_ (x):
    ele, val= x.replace('+', ' +').split() if '+' in x else x.replace('-', ' -').split()     
    return ele.capitalize(), int(val)    
    
lista=[]    
for index,cation in enumerate(_sBVS):
    cat, vcat= _name1_(cation)
    for an_i,an_p in enumerate(map(list, list(zip(*_sBVS[cation])))):
        Anion, VAnion = _name1_(_sBVS_anions[an_i])
        if an_p[0]:
            lista.append({"Cat":cat,"VCat":vcat,"Anion":Anion, "VAnion":VAnion,
                         "Ro":float(an_p[0]), "B":float(an_p[1]),
                         "Cn":float(an_p[2]), "ctoff":float(an_p[3]),
                         "Ref":_valence_ref_id[an_p[4]], "Index":index })
######################################################




  
class vbs_database(list):
   """lista modificata che contiene per ogni
      elemento un dizionatio per ogni linea del database
   """
   def __repr__(self):
      if len(self)==0:
           return "Empty list of available parameter"
      a= "Index, Cat, VCat , Anion, VAnion, Ro, B, Ref,Notes \n"
      for item in self.__iter__(): 
           a+=" ".join(map(str,[item["Index"] , item["Cat"], item["VCat"] ,
           item["Anion"], item["VAnion"], item["Ro"], item["B"],
           item["Ref"], item["Notes"]]))
           a+="\n"
      #print b     
      return a

   def __getslice__(self, *args):
       print('get', args)           
       a=super(vbs_database, self).__getslice__(*args)
       return vbs_database(a)
       
   def search_bvp(self,Cat=None,VCat=None,Anion=None,VAnion=None):
       """create a reduced list that contains the value inserted
       """
       _illor  = lambda item,key,value: True if value==None else item[key]==value   
       reduced_list=vbs_database([item for item in self if \
            _illor(item,"Cat",Cat) and _illor(item,"VCat",VCat) and \
            _illor(item,"Anion",Anion) and _illor(item,"VAnion",VAnion)])
       return reduced_list
       
   def _search_Index(self,Index):
       try:
           Index= Index if self[Index]["Index"]==Index else \
                 [self.index(item) for item in self if item["Index"]==Index].pop()
       except IndexError as e:
           a=[self.index(item) for item in self if item["Index"]==Index]
           if a :Index=a.pop() 
           else: return False
       return Index    
    
   def _cal_vi(self, Index,Ri):
       """last value in tha arguments is the distance
       """
       Index=self._search_Index(Index)
       
       if isinstance(Index, bool):
           return Index          
       else:  
           vi= math.exp((self[Index]["Ro"]-Ri)/self[Index]["B"])
           return vi      
       
   def _cal_Ri(self, Index,vi):
       """last value in tha arguments is the distance in Angstrom
       """
       Index=self._search_Index(Index)
       if isinstance(Index, bool):
           return Index 
       else:
           Ri= self[Index]["Ro"]-math.log(vi)*self[Index]["B"]
           return Ri
       
   def cal_BD(self, *Args):
       """
       REturn idela Bond distance
          2 argument Index and vi 
                 database index and distance
          5 argument "Cat" "VCat" "Anion" "VAnion" vi 
                 used first possibility in he database
       """
       if len(Args)==2:
           Index=Args[0]
       if len(Args)==5 :
           try:
               Index=self.search_bvp(Cat=Args[0],VCat=Args[1],
                                 Anion=Args[2],VAnion=Args[3])[0]["Index"]
           except IndexError:
               return self.search_bvp(Cat=Args[0],VCat=Args[1],
                                 Anion=Args[2],VAnion=Args[3])
       vi=Args[-1]
       Ri=self._cal_Ri(Index,vi) 
       if Ri:
           print("Optimal distance=", round(Ri,3), "Angstrom for ",\
                       round(valence_param[Index]["VCat"]/vi,2), \
                       valence_param[Index]["Anion"], " around ",\
                       valence_param[Index]["Cat"])
       else: print("parameter not available in the database")                
       return 
       
           
   def cal_BV(self, *Args):
       """
          2 argument Index and Distance
                 database index and distance
          5 argument "Cat" "VCat" "Anion" "VAnion" Distance
                 used first possibility in he database
       """
       if len(Args)==2:
           Index=Args[0]
       if len(Args)==5 :
           try:
               Index=self.search_bvp(Cat=Args[0],VCat=Args[1],
                                 Anion=Args[2],VAnion=Args[3])[0]["Index"]
           except IndexError:
               return self.search_bvp(Cat=Args[0],VCat=Args[1],
                                 Anion=Args[2],VAnion=Args[3])
       Dis=Args[-1]           
       vi=self._cal_vi(Index,Dis)
       if vi:
           print("vi=",round(vi,3), "  optimal coordinance=", \
                       round(valence_param[Index]["VCat"]/vi,2), \
                       valence_param[Index]["Anion"], "  around   ",\
                       valence_param[Index]["Cat"])
       else: print("parameter not available in the database")                
       return  

       

s_softBV =vbs_database(lista)
    
valence_param =vbs_database([{"Cat":item[0],"VCat":int(item[1]),"Anion":item[2], "VAnion":int(item[3]),
                "Ro":float(item[4]), "B":float(item[5]), "Ref":_valence_ref_id[item[6]],
                "Notes":item[7], "Index":lines.index(item)} for item in lines])



del  lines, lista

if __name__ == "__main__":
    print("Bond valence method Sum calculator")
    while True:
        formula  = input("\n######################################\nWrite Cation and Anion without charge"+\
                             "or type quit to exit\nexample:   Nd   S\n")
        if formula =="quit": break
        Cat,Ani=formula.split()
        redlist=valence_param.search_bvp(Cat=Cat, Anion=Ani)
        print(30*"*")
        print("\nResults of the search")
        print(redlist)
        while True: 
            print(30*"#*")
            print("To calculate expected bond lenght  type: B Index and valence_bond")
            print("To calculate expected valence_bond type: V Index and bond_lenght")
            print("To repeat a search type: S")
            print("To exit type: quit")
            formula=input("")
            if formula =="quit": break
            if formula =="S": 
                print("\n"*10)
                break
            if formula.split()[0]=="B":
                print(formula.split()[1],formula.split()[2])
                redlist.cal_BD(int(formula.split()[1]),float(formula.split()[2]))
            if formula.split()[0]=="V":
                redlist.cal_BV(int(formula.split()[1]),float(formula.split()[2]))    
            print("\n")    
        if formula =="quit": break           