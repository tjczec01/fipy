#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - a finite volume PDE solver in Python
 # 
 #  FILE: "test.py"
 #                                    created: 7/28/04 {11:18:34 AM} 
 #                                last update: 4/1/05 {2:47:18 PM} 
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This document was prepared at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this document is not subject to copyright
 # protection and is in the public domain.  test.py
 # is an experimental work.  NIST assumes no responsibility whatsoever
 # for its use by other parties, and makes no guarantees, expressed
 # or implied, about its quality, reliability, or any other characteristic.
 # We would appreciate acknowledgement if the document is used.
 # 
 # This document can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  See the file "license.terms" for information on usage and  redistribution of this file, and for a DISCLAIMER OF ALL WARRANTIES.
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2004-07-28 JEG 1.0 original
 # ###################################################################
 ##

from fipy.tests.doctestPlus import LateImportDocTestSuite
import fipy.tests.testProgram

def _suite():
    return LateImportDocTestSuite(docTestModuleNames = (
            'diffusion.input1D',
            'diffusion.input1Ddimensional',
            'diffusion.input2D',
            'diffusion.input2Dcorner',
            'phase.input1D',
            'phaseDiffusion.input1Dbinary',
            'phaseDiffusion.input1Dquaternary',
            'phaseDiffusion.input1DternaryAndElectrons',
            'poisson.input1DallCharge',
            'poisson.input1DleftCharge',
            'poisson.input1DrightCharge'
        ), base = __name__)
    
if __name__ == '__main__':
    fipy.tests.testProgram.main(defaultTest='_suite')

