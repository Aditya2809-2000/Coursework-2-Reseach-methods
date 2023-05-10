{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 272,
   "id": "d4f563ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
   "id": "a2bb32ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "#loading the data\n",
    "australia = pd.read_csv('AUSdeath.txt')\n",
    "germany = pd.read_csv('DEUTNPdeath.txt')\n",
    "canada = pd.read_csv('CANdeath.txt')\n",
    "russia = pd.read_csv('RUSdeath.txt')\n",
    "usa = pd.read_csv('USAdeath.txt')\n",
    "portugal = pd.read_csv('PRtdeath.txt')\n",
    "france = pd.read_csv('FRATNPdeath.txt')\n",
    "newzealand = pd.read_csv('NZL_NPdeath.txt')\n",
    "ireland = pd.read_csv('IRLdeath.txt')\n",
    "israel = pd.read_csv('ISRdeath.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "id": "b6a88e72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1948 1949 1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961\n",
      " 1962 1963 1964 1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975\n",
      " 1976 1977 1978 1979 1980 1981 1982 1983 1984 1985 1986 1987 1988 1989\n",
      " 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003\n",
      " 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017\n",
      " 2018 2019 2020 2021]\n"
     ]
    }
   ],
   "source": [
    "# finding unique years\n",
    "\n",
    "nz = newzealand['Year'].unique()\n",
    "print(nz)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "id": "8697f142",
   "metadata": {},
   "outputs": [],
   "source": [
    "isr = israel['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "id": "35c0f1f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "ire = ireland['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 277,
   "id": "c72523a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "frn = france['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 278,
   "id": "045a3d1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "por = portugal['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "id": "b1a56764",
   "metadata": {},
   "outputs": [],
   "source": [
    "aus = australia['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 280,
   "id": "ddcca201",
   "metadata": {},
   "outputs": [],
   "source": [
    "ger = germany['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "id": "ffa54814",
   "metadata": {},
   "outputs": [],
   "source": [
    "can = canada['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 282,
   "id": "4c15dd65",
   "metadata": {},
   "outputs": [],
   "source": [
    "russ = russia['Year'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 283,
   "id": "3a306f2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "us = usa['Year'].unique() \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 284,
   "id": "47e2e1a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014}\n"
     ]
    }
   ],
   "source": [
    "# Searching for common years in the data \n",
    "intersection = set(us).intersection(russ).intersection(can).intersection(ger).intersection(aus).intersection(por).intersection(frn).intersection(ire).intersection(isr).intersection(nz)\n",
    "print(intersection)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b328fb71",
   "metadata": {},
   "source": [
    "# Counting Number of Deaths in popular 10 countries in 1999"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "id": "66072e43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 285,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(australia['Deaths'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "id": "d35509ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "aus PopName         AUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSA...\n",
      "Area                                                          845\n",
      "Year                                                      1689155\n",
      "YearReg                                                   1689155\n",
      "YearInterval                                                  845\n",
      "Sex             ffffffffffffffffffffffffffffffffffffffffffffff...\n",
      "Age             0000111122223333444455556666777788889999101010...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           RRRRTLTURRRRTLTURRRRTLTURRRRTLTURRRRTLTURRRRTL...\n",
      "RefCode                                                     17993\n",
      "Access          OOOOOOOOOOOOCOOOOOOOOOOOOOOOOOOOOOOOCOOOCOOOOO...\n",
      "Deaths          1731135377671210125207431592462099621312426567...\n",
      "NoteCode1       ............1.11........................1.11.....\n",
      "NoteCode2       .................................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           624\n",
      "dtype: object\n",
      "can PopName         CANCANCANCANCANCANCANCANCANCANCANCANCANCANCANC...\n",
      "Area                                                          718\n",
      "Year                                                      1435282\n",
      "YearReg                                                   1435282\n",
      "YearInterval                                                  718\n",
      "Sex             ffffffffffffffffffffffffffffffffffffffffffffff...\n",
      "Age                                                         42840\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           TLTURRTLTURRTLTURRTLTURRTLTURRTLTURRTLTURRTLTU...\n",
      "RefCode                                                       718\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                                   219530.0\n",
      "NoteCode1       .................................................\n",
      "NoteCode2       .................................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           718\n",
      "dtype: object\n",
      "rus PopName         RUSRUSRUSRUSRUSRUSRUSRUSRUSRUSRUSRUSRUSRUSRUSR...\n",
      "Area                                                         2472\n",
      "Year                                                       411794\n",
      "YearReg                                                    411794\n",
      "YearInterval                                                  206\n",
      "Sex             mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm...\n",
      "Age             0123456789101112131415161718192021222324252627...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR...\n",
      "RefCode                                                       206\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                                  4288632.0\n",
      "NoteCode1       .................................................\n",
      "NoteCode2       .................................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           206\n",
      "dtype: object\n",
      "ger PopName         DEUTNPDEUTNPDEUTNPDEUTNPDEUTNPDEUTNPDEUTNPDEUT...\n",
      "Area                                                          464\n",
      "Year                                                       927536\n",
      "YearReg                                                    927536\n",
      "YearInterval                                                  464\n",
      "Sex             ffffffffffffffffffffffffffffffffffffffffffffff...\n",
      "Age             0011223344556677889910101111121213131414151516...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           TLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTL...\n",
      "RefCode         7777777777777777777777777777777777777777777777...\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                                    1692660\n",
      "NoteCode1       3333333333333333333333333333333333333333333333...\n",
      "NoteCode2       4444444444444444444444444444444444444444444444...\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           464\n",
      "dtype: object\n",
      "usa PopName         USAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAUSAU...\n",
      "Area                                                          449\n",
      "Year                                                       897551\n",
      "YearReg                                                    897551\n",
      "YearInterval                                                  449\n",
      "Sex             ffffffffffffffffffffffffffffffffffffffffffffff...\n",
      "Age             0011223344556677889910101111121213131414151516...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           TLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTL...\n",
      "RefCode                                                    113390\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                             2391399.000005\n",
      "NoteCode1       .................................................\n",
      "NoteCode2       .................................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           449\n",
      "dtype: object\n",
      "fra PopName         FRATNPFRATNPFRATNPFRATNPFRATNPFRATNPFRATNPFRAT...\n",
      "Area                                                        45000\n",
      "Year                                                       999500\n",
      "YearReg                                                    999500\n",
      "YearInterval                                                  500\n",
      "Sex             ffffffffffffffffffffffffffffffffffffffffffffff...\n",
      "Age             0011223344556677889910101111121213131414151516...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           TLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTL...\n",
      "RefCode                                                   15500.0\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                                     537661\n",
      "NoteCode1       .................................................\n",
      "NoteCode2       .................................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           500\n",
      "dtype: object\n",
      "isr PopName         ISRISRISRISRISRISRISRISRISRISRISRISRISRISRISRI...\n",
      "Area                                                          196\n",
      "Year                                                       391804\n",
      "YearReg                                                    391804\n",
      "YearInterval                                                  196\n",
      "Sex             mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm...\n",
      "Age             0123456789101112131415161718192021222324252627...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR...\n",
      "RefCode                                                       588\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                                      74580\n",
      "NoteCode1       .................................................\n",
      "NoteCode2       .................................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           196\n",
      "dtype: object\n",
      "ire PopName         IRLIRLIRLIRLIRLIRLIRLIRLIRLIRLIRLIRLIRLIRLIRLI...\n",
      "Area                                                          218\n",
      "Year                                                       435782\n",
      "YearReg                                                    435782\n",
      "YearInterval                                                  218\n",
      "Sex             mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm...\n",
      "Age             0123456789101112131415161718192021222324252627...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR...\n",
      "RefCode                                                      2180\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                                      65216\n",
      "NoteCode1                                                    1744\n",
      "NoteCode2       .................................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           218\n",
      "dtype: object\n",
      "nz PopName         NZL_NPNZL_NPNZL_NPNZL_NPNZL_NPNZL_NPNZL_NPNZL_...\n",
      "Area                                                         9960\n",
      "Year                                                       995502\n",
      "YearReg                                                    995641\n",
      "YearInterval                                                  498\n",
      "Sex             ffffffffffffffffffffffffffffffffffffffffffffff...\n",
      "Age             0001122334455667788991010111112121313141415151...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           TLTUVHTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTU...\n",
      "RefCode                                                      4516\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                                      28133\n",
      "NoteCode1                                                    4980\n",
      "NoteCode2       12.12............................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           498\n",
      "dtype: object\n",
      "portugal PopName         PRTPRTPRTPRTPRTPRTPRTPRTPRTPRTPRTPRTPRTPRTPRTP...\n",
      "Area                                                         4020\n",
      "Year                                                       803598\n",
      "YearReg                                                    803598\n",
      "YearInterval                                                  402\n",
      "Sex             ffffffffffffffffffffffffffffffffffffffffffffff...\n",
      "Age             0011223344556677889910101111121213131414151516...\n",
      "AgeInterval     1111111111111111111111111111111111111111111111...\n",
      "Lexis           TLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTLTUTL...\n",
      "RefCode                                                      4824\n",
      "Access          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO...\n",
      "Deaths                                                   107871.0\n",
      "NoteCode1       .................................................\n",
      "NoteCode2       .................................................\n",
      "NoteCode3       .................................................\n",
      "LDB                                                           402\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print('aus',australia[australia['Year'] == 1999].sum())\n",
    "print('can',canada[canada['Year'] == 1999].sum())\n",
    "print('rus',russia[russia['Year'] == 1999].sum())\n",
    "print('ger',germany[germany['Year'] == 1999].sum())\n",
    "print('usa',usa[usa['Year'] == 1999].sum())\n",
    "print('fra',france[france['Year'] == 1999].sum())\n",
    "print('isr',israel[israel['Year'] == 1999].sum())\n",
    "print('ire',ireland[ireland['Year'] == 1999].sum())\n",
    "print('nz',newzealand[newzealand['Year'] == 1999].sum())\n",
    "print('portugal',portugal[portugal['Year'] == 1999].sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a8460ed6",
   "metadata": {},
   "source": [
    "# Finding Male and Female data for the year 1999\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 240,
   "id": "a852e2b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male germany 911176\n",
      "female germany 781484\n"
     ]
    }
   ],
   "source": [
    "print('Male germany',germany[(germany['Year'] == 1999) & (germany['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female germany',germany[(germany['Year'] == 1999) & (germany['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "id": "f86358cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male canada 105859.0\n",
      "female canada 113671.0\n"
     ]
    }
   ],
   "source": [
    "print('Male canada',canada[(canada['Year'] == 1999) & (canada['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female canada',canada[(canada['Year'] == 1999) & (canada['Sex'] == 'm')]['Deaths'].sum())\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "c1644cdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male france 262801\n",
      "female france 274860\n"
     ]
    }
   ],
   "source": [
    "print('Male france',france[(france['Year'] == 1999) & (france['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female france',france[(france['Year'] == 1999) & (france['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "48c91a05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male portugal 51692.0\n",
      "female portugal 56179.0\n"
     ]
    }
   ],
   "source": [
    "print('Male portugal',portugal[(portugal['Year'] == 1999) & (portugal['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female portugal',portugal[(portugal['Year'] == 1999) & (portugal['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "eaff7b48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male ireland 31294\n",
      "female ireland 33922\n"
     ]
    }
   ],
   "source": [
    "print('Male ireland',ireland[(ireland['Year'] == 1999) & (ireland['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female ireland',ireland[(ireland['Year'] == 1999) & (ireland['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "id": "ce4ca71f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male israel 36910\n",
      "female israel 37670\n"
     ]
    }
   ],
   "source": [
    "print('Male israel',israel[(israel['Year'] == 1999) & (israel['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female israel',israel[(israel['Year'] == 1999) & (israel['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "id": "0f236387",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male newzealand 13849\n",
      "female newzealand 14284\n"
     ]
    }
   ],
   "source": [
    "print('Male newzealand',newzealand[(newzealand['Year'] == 1999) & (newzealand['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female newzealand',newzealand[(newzealand['Year'] == 1999) & (newzealand['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "id": "c0139a00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male portugal 51692.0\n",
      "female portugal 56179.0\n"
     ]
    }
   ],
   "source": [
    "print('Male portugal',portugal[(portugal['Year'] == 1999) & (portugal['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female portugal',portugal[(portugal['Year'] == 1999) & (portugal['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "id": "22354d68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male russia 2063590.0\n",
      "female russia 2225042.0\n"
     ]
    }
   ],
   "source": [
    "print('Male russia',russia[(russia['Year'] == 1999) & (russia['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female russia',russia[(russia['Year'] == 1999) & (russia['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 314,
   "id": "914dda63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Male usa 1215939.000001\n",
      "female usa 58235.39\n"
     ]
    }
   ],
   "source": [
    "print('Male usa',usa[(usa['Year'] == 1999) & (usa['Sex'] == 'f')]['Deaths'].sum())\n",
    "print('female usa',usa[(russia['Year'] == 1999) & (usa['Sex'] == 'm')]['Deaths'].sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db0d7a70",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for australia the data was not in the suitable datatype so I have used excel to attain the desired data."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
