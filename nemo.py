# -*- coding: utf-8 -*-
# Nemo is a regression Kriging code written in Python.
# Copyright (C) 2011 Farnaz Heidar Zadeh <farnaz_chem@yahoo.com>, Toon
# Verstraelen <Toon.Verstraelen@UGent.be>, Paul Ayers <ayers@mcmaster.ca>; all
# rights reserved unless otherwise stated.
#
# This file is part of Nemo.
#
# Nemo is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# Nemo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --
'''
TODO: General background.
'''

import numpy as np


class Kriging(object):
    def __init__(self, names, dm, ev, sms):
        '''Create a Kriging object.
        
           Arguments:

           names
                A list of strings describing the rows of the design matrix.
                (length = nrows)

           dm
                A design matrix for the linear regression part of the Kriging.
                (shape = nrows, npars)
           
           ev
                The expected values for the linear regression part of the
                Kriging. (shape = nrows)

           sms
                A list of similarity matrices for the Kriging. For each matrix
                in this list: shape = nrows, nrows.
        '''
        self.names = names
        self.dm = dm
        self.ev = ev
        self.sms = sms
        self.calibrate_model()
    
    def calibrate_model(self):
        pass
    
    def __call__(self, knowns, similarities):
        return self.predict_linear_part(knowns) + self.predict_kriging(similarities)
    
    def predict_linear_part(self, knowns):
        pass

    def predict_kriging(similarities):
        pass

    def cross_validation(self, fn_out=None):
        '''Perform a cross validation test.
        
           Arguments:
           
           fn_out
                Optional output file. If not given the results are printed on
                screen.
           
           All information for the cross validation is
           contained in the attributes of this class.
           
           This method returns the average of the squared error between the
           predicted value and the expected value, where the prediction is made
           by a model that does not include the expected value. (This is
           leave-one-out cross validation.)
        '''
        if fn_out is None:
            f = sys.stdout
        else:
            f = file(fn_out, 'w')
        
        result = 0.0
        for i in xrange(len(self.names)):
            small_sms = []
            for sm in self.sms:
                small_sm = np.zeros((len(self.names)-1, len(self.names)-1), float)
                small_sm[:i,:i] = sm[:i,:i]
                small_sm[:i,i:] = sm[:i,:i+1]
                small_sm[i:,:i] = sm[i+1:,:i]
                small_sm[i:,i:] = sm[i+1:,i+1:]
                small_sms.append(small_sm)
            small_model = Kriging(
                self.names[:i] + self.names[i+1:],
                np.concatenate(self.dm[:i], self.dm[i+1:]),
                np.concatenate(self.ev[:i], self.ev[i+1:]),
                small_sms
            )
            predicted_value = small_model(self.dm[i], [sm[i] for sm in self.sms])
            expected_value = self.evs[i]
            result += (predicted_value-expected_value)**2
        
        print >> f, 'The mean square error is %10.5e' % result
        log('The mean square error is %10.5e' % result)
        
        if fn_out is not None:
            f.close()
        return result/len(self.names)





