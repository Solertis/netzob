# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Global Imports
#+---------------------------------------------------------------------------+
import logging
import gtk
import pygtk
import gobject

pygtk.require('2.0')

#+---------------------------------------------------------------------------+
#| Local Imports
#+---------------------------------------------------------------------------+


#+----------------------------------------------
#| AutomaticGrammarAbstractionView:
#|     Class to show the wizard and to abstract the current gramar
#+----------------------------------------------
class AutomaticGrammarAbstractionView(object):

    #+----------------------------------------------
    #| Constructor:
    #+----------------------------------------------
    def __init__(self, project):
        # create logger with the given configuration
        self.log = logging.getLogger('netzob.Inference.Grammar.AutomaticGrammarAbstractionView.py')
        self.project = project

    def display(self):
        # Display the form for the creation of a word variable
        self.dialog = gtk.Dialog(title="Automatic abstraction of the current grammar", flags=0, buttons=None)

        mainTable = gtk.Table(rows=2, columns=2, homogeneous=False)
        # Insert the Save button
        self.startButton = gtk.Button("Start the abstraction")
        self.startButton.show()
        self.startButton.connect("clicked", self.startAbstraction)
        mainTable.attach(self.startButton, 0, 2, 0, 1, xoptions=gtk.FILL, yoptions=0, xpadding=5, ypadding=5)
        self.dialog.vbox.pack_end(mainTable, True, True, 0)
        self.dialog.show_all()

    def startAbstraction(self, button):
        self.log.debug("Start the abstraction")
        
        # Retrieve available sequences
        sessions = self.project.getVocabulary().getSessions()
        self.log.debug("A number of %d sessions will be injected in the grammar" % (len(sessions)))
        
        for session in sessions :
            self.log.debug("Search for a difference with a new session")
            # We apply the session on current automata and find an output symbol to include
            difference = self.applySession(session)
            while difference != None :
                (transition, outputSymbol) = difference
                self.log.debug("A difference has been found, symbol %s must be added to transition %s" % (outputSymbol.getName(), transition.getName()))
                self.addOutputSymbolOnTransition(outputSymbol, transition)
                difference = self.applySession(session)
            self.log.debug("The current session does not introduce other differences")
        
        self.log.debug("All the sessions have been applied on current automata")
        
    def addOutputSymbolOnTransition(self, symbol, transition):
        pass    
    
    def applySession(self, session):
        # retrieve the automata
        automata = self.project.getGrammar().getAutomata()
        if automata == None :
            self.log.warn("Cannot apply a session on the current automata because it doesn't exist")
            return None
        
        difference = None
        
        return difference            
                
                
            
            
        