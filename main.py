import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from mainwindow import Ui_MainWindow

class R_Phylo(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super (R_Phylo, self).__init__(parent)  
		self.createWidget()
		
	def createWidget(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# setting up database connection for model
		self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName('as.db')
		self.db.open()

		self.initData1()
		self.initData2()
		self.connectCBoxes()
		self.ui.comboBox_8.editTextChanged.connect(self._handleC7Change)
		self.ui.comboBox_15.editTextChanged.connect(self._handleC8Change)
		self.ui.comboBox_16.editTextChanged.connect(self._handleC9Change)
		self.ui.comboBox_17.editTextChanged.connect(self._handleC10Change)
		self.ui.pushButton.clicked.connect(self._handleBChange)
		self.ui.pushButton_2.clicked.connect(self._handleB2Change)
		self.ui.pushButton_3.clicked.connect(self._handleB3Change)
		self.ui.tableView.doubleClicked.connect(self._handleTChange)
		self.ui.tableView_3.doubleClicked.connect(self._handleT2Change)
		self.ui.textEdit.setReadOnly(1)
	
	def initData1(self):
		# defining SQL queries
		# TAB1
		# Object	PyQT_name	object_model	object_query	event			
		# main_table	tableView	model		query		
		# cbox_genus	comboBox	model2		query2		C1
		# cbox_species	comboBox_2	model3		query3		C2
		# cbox_family	comboBox_3	model4		query4		C3
		# cbox_order	comboBox_4	model5		query5		C4
		# cbox_class	comboBox_5	model6		query6		C5
		# cbox_phylum	comboBox_6	model7		query7		C6
		# popup_table	tableView_2	model8		query8		T	
		# 

	#TAB1 ---------------------------------------------------------------------------------
		# main_table
		self.model = QtSql.QSqlQueryModel(self)
		query=QtSql.QSqlQuery("select code_art, lib1_art, lib2_art, four_art from abl_art order by lib1_art, lib2_art")
		self.model.setQuery(query)
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Code")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Libellé")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Libellé 2")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Fournisseur")
		self.ui.tableView.setModel(self.model)
		self.ui.tableView.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
		self.ui.tableView.verticalHeader().setVisible(False)

		# cbox_genus
		self.model2 = QtSql.QSqlTableModel()
		#TAF : joindre les genres ABL orphelins outer join
		query2=QtSql.QSqlQuery("select uid, case when o.nb_abl>0 then upper(o.name)||' '||'('||o.nb_abl||')' else upper(o.name) end as cgenus"+
			" from ott_taxa o where o.rank='genus' order by cgenus")
		self.model2.setQuery(query2)		
		self.ui.comboBox.setModel(self.model2)
		self.ui.comboBox.setModelColumn(self.model2.fieldIndex("cgenus"))
		self.ui.comboBox.setEditable(True)
		self.ui.comboBox.setInsertPolicy(0)


		# cbox_species
		self.model3 = QtSql.QSqlTableModel()
		query3=QtSql.QSqlQuery("select espece_art from abl_art group by espece_art order by espece_art	")
		self.model3.setQuery(query3)		
		self.ui.comboBox_2.setModel(self.model3)
		self.ui.comboBox_2.setModelColumn(self.model3.fieldIndex("espece_art"))
		self.ui.comboBox_2.setEditable(True)
		self.ui.comboBox_2.setInsertPolicy(0)


		# cbox_family
		self.model4 = QtSql.QSqlTableModel()
		query4=QtSql.QSqlQuery("select uid, case when nb_abl>0 then name||' '||'('||nb_abl||')' else name end as cname"+
			" from ott_taxa h where rank='family' order by name")
		self.model4.setQuery(query4)		
		self.ui.comboBox_3.setModel(self.model4)
		self.ui.comboBox_3.setModelColumn(self.model4.fieldIndex("cname"))
		self.ui.comboBox_3.setEditable(True)
		self.ui.comboBox_3.setInsertPolicy(0)



		# cbox_order
		self.model5 = QtSql.QSqlTableModel()
		query5=QtSql.QSqlQuery("select uid, case when nb_abl>0 then name||' '||'('||nb_abl||')' else name end as cname"+
			" from ott_taxa h where rank='order' order by name")
		self.model5.setQuery(query5)		
		self.ui.comboBox_4.setModel(self.model5)
		self.ui.comboBox_4.setModelColumn(self.model5.fieldIndex("cname"))
		self.ui.comboBox_4.setEditable(True)
		self.ui.comboBox_4.setInsertPolicy(0)


		# cbox_class
		self.model6 = QtSql.QSqlTableModel()
		query6=QtSql.QSqlQuery("select uid, case when nb_abl>0 then name||' '||'('||nb_abl||')' else name end as cname"+
			" from ott_taxa h where rank='class' order by name")
		self.model6.setQuery(query6)		
		self.ui.comboBox_5.setModel(self.model6)
		self.ui.comboBox_5.setModelColumn(self.model6.fieldIndex("cname"))
		self.ui.comboBox_5.setEditable(True)
		self.ui.comboBox_5.setInsertPolicy(0)


		# cbox_phylum
		self.model7 = QtSql.QSqlTableModel()
		query7=QtSql.QSqlQuery("select uid, case when nb_abl>0 then name||' '||'('||nb_abl||')' else name end as cname"+
			" from ott_taxa h where rank='phylum' order by name")
		self.model7.setQuery(query7)		
		self.ui.comboBox_6.setModel(self.model7)
		self.ui.comboBox_6.setModelColumn(self.model7.fieldIndex("cname"))
		self.ui.comboBox_6.setEditable(True)
		self.ui.comboBox_6.setInsertPolicy(0)

		#table popup
		self.model8 = QtSql.QSqlQueryModel()
		self.ui.tableView_2.setModel(self.model8)
		self.ui.tableView_2.hide()

		self.ui.comboBox.setEditText("")
		self.ui.comboBox_2.setEditText("")
		self.ui.comboBox_3.setEditText("")
		self.ui.comboBox_4.setEditText("")
		self.ui.comboBox_5.setEditText("")
		self.ui.comboBox_6.setEditText("")


	def initData2(self):
	#TAB2 ---------------------------------------------------------------------------------
		# TAB2
		# Object	PyQT_name	object_model	object_query	event			
		# main_table	tableView_3	model11		query11		
		# cbox_genus	comboBox_7	model12		query12		
		# cbox_species	comboBox_8	model13		query13		C7
		# cbox_variety	comboBox_9	model14		query14		
		# cbox_four	comboBox_10	model15		query15		
		# cbox_tpot	comboBox_11	model16		query16		
		# cbox_mpot	comboBox_12	model17		query17			
		# cbox_cdt	comboBox_13	model19		query19
		# cbox_haut	comboBox_22	model20		query20		
		# cbox_mix	comboBox_20	model21		query21		
		# cbox_forme	comboBox_14	model22		query22		
		# cbox_coul	comboBox_19	model23		query23	
		# cbox_meta1	comboBox_15	model24		query24		C8
		# cbox_meta11	comboBox_23	model25		query25	
		# cbox_meta2	comboBox_16	model26		query26		C9
		# cbox_meta22	comboBox_24	model27		query27	
		# cbox_meta3	comboBox_17	model28		query28		C10
		# cbox_meta33	comboBox_25	model29		query29	


		# main_table
		self.model11 = QtSql.QSqlQueryModel(self)
		query11=QtSql.QSqlQuery("select art_code, art_tpot_fk, art_mpot, art_forme_pot, art_four, art_cdtplat, art_hb, art_hh, art_coul, art_forme from abl_art2 order by art_four, art_tpot_fk, art_mpot")
		self.model11.setQuery(query11)
		self.model11.setHeaderData(0, QtCore.Qt.Horizontal, "Code")
		self.model11.setHeaderData(1, QtCore.Qt.Horizontal, "Diamètre/litrage")
		self.model11.setHeaderData(2, QtCore.Qt.Horizontal, "Mesure Pot")
		self.model11.setHeaderData(3, QtCore.Qt.Horizontal, "Type pot")
		self.model11.setHeaderData(4, QtCore.Qt.Horizontal, "Fournisseur")
		self.model11.setHeaderData(5, QtCore.Qt.Horizontal, "x")
		self.model11.setHeaderData(6, QtCore.Qt.Horizontal, "H min")
		self.model11.setHeaderData(7, QtCore.Qt.Horizontal, "H max")
		self.model11.setHeaderData(8, QtCore.Qt.Horizontal, "Couleur")
		self.model11.setHeaderData(9, QtCore.Qt.Horizontal, "Forme")
		self.ui.tableView_3.setModel(self.model11)
		self.ui.tableView_3.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
		self.ui.tableView_3.verticalHeader().setVisible(False)

		# cbox_genus
		self.model12 = QtSql.QSqlTableModel()
		query12=QtSql.QSqlQuery("select iuid, i_name from "+'"'+"ABL_TAXA"+'"'+" where i_rank='GENRE' order by i_name")
		self.model12.setQuery(query12)		
		self.ui.comboBox_7.setModel(self.model12)
		self.ui.comboBox_7.setModelColumn(self.model12.fieldIndex("i_name"))
		self.ui.comboBox_7.setEditable(True)
		self.ui.comboBox_7.setInsertPolicy(0)

		# cbox_species
		self.model13 = QtSql.QSqlTableModel()
		query13=QtSql.QSqlQuery("select iuid, i_name, case when nb_abl>0 then i_name||' ('||nb_abl||')' else i_name end as cname from "+'"'+"ABL_TAXA"+'"'+" where i_rank='espèce' order by i_name")
		self.model13.setQuery(query13)		
		self.ui.comboBox_8.setModel(self.model13)
		self.ui.comboBox_8.setModelColumn(self.model13.fieldIndex("cname"))
		self.ui.comboBox_8.setEditable(True)
		self.ui.comboBox_8.setInsertPolicy(0)

		# cbox_var
		self.model14 = QtSql.QSqlTableModel()
		query14=QtSql.QSqlQuery("select iuid, i_name from "+'"'+"ABL_TAXA"+'"'+" where i_rank='Variété' order by i_name")
		self.model14.setQuery(query14)		
		self.ui.comboBox_9.setModel(self.model14)
		self.ui.comboBox_9.setModelColumn(self.model14.fieldIndex("i_name"))
		self.ui.comboBox_9.setEditable(True)
		self.ui.comboBox_9.setInsertPolicy(0)

		# cbox_four
		self.model15 = QtSql.QSqlTableModel()
		query15=QtSql.QSqlQuery("select art_four from abl_art2 group by art_four order by art_four")
		self.model15.setQuery(query15)		
		self.ui.comboBox_10.setModel(self.model15)
		self.ui.comboBox_10.setModelColumn(self.model15.fieldIndex("art_four"))
		self.ui.comboBox_10.setEditable(True)
		self.ui.comboBox_10.setInsertPolicy(0)

		# cbox_tpot
		self.model16 = QtSql.QSqlTableModel()
		query16=QtSql.QSqlQuery("select art_tpot_fk from abl_art2 group by art_tpot_fk order by art_tpot_fk")
		self.model16.setQuery(query16)		
		self.ui.comboBox_11.setModel(self.model16)
		self.ui.comboBox_11.setModelColumn(self.model16.fieldIndex("art_tpot_fk"))
		self.ui.comboBox_11.setEditable(True)
		self.ui.comboBox_11.setInsertPolicy(0)

		# cbox_mpot
		self.model17 = QtSql.QSqlTableModel()
		query17=QtSql.QSqlQuery("select art_mpot from abl_art2 group by art_mpot order by art_mpot")
		self.model17.setQuery(query17)		
		self.ui.comboBox_12.setModel(self.model17)
		self.ui.comboBox_12.setModelColumn(self.model17.fieldIndex("art_mpot"))
		self.ui.comboBox_12.setEditable(True)
		self.ui.comboBox_12.setInsertPolicy(0)

		# cbox_cdt
		self.model19 = QtSql.QSqlTableModel()
		query19=QtSql.QSqlQuery("select art_cdtplat from abl_art2 group by art_cdtplat order by art_cdtplat")
		self.model19.setQuery(query19)		
		self.ui.comboBox_13.setModel(self.model19)
		self.ui.comboBox_13.setModelColumn(self.model19.fieldIndex("art_cdtplat"))
		self.ui.comboBox_13.setEditable(True)
		self.ui.comboBox_13.setInsertPolicy(0)

		# cbox_hauteur
		self.model20 = QtSql.QSqlTableModel()
		query20=QtSql.QSqlQuery("select art_hb from abl_art2 group by art_hb order by art_hb")
		self.model20.setQuery(query20)		
		self.ui.comboBox_22.setModel(self.model20)
		self.ui.comboBox_22.setModelColumn(self.model20.fieldIndex("art_hb"))
		self.ui.comboBox_22.setEditable(True)
		self.ui.comboBox_22.setInsertPolicy(0)

		# cbox_mix
		self.model21 = QtSql.QSqlTableModel()
		query21=QtSql.QSqlQuery("select art_mix from abl_art2 group by art_mix order by art_mix")
		self.model21.setQuery(query21)		
		self.ui.comboBox_20.setModel(self.model21)
		self.ui.comboBox_20.setModelColumn(self.model21.fieldIndex("art_mix"))
		self.ui.comboBox_20.setEditable(True)
		self.ui.comboBox_20.setInsertPolicy(0)

		# cbox_forme
		self.model22 = QtSql.QSqlTableModel()
		query22=QtSql.QSqlQuery("select art_forme from abl_art2 group by art_forme order by art_forme")
		self.model22.setQuery(query22)		
		self.ui.comboBox_14.setModel(self.model22)
		self.ui.comboBox_14.setModelColumn(self.model22.fieldIndex("art_forme"))
		self.ui.comboBox_14.setEditable(True)
		self.ui.comboBox_14.setInsertPolicy(0)

		# cbox_couleur
		self.model23 = QtSql.QSqlTableModel()
		query23=QtSql.QSqlQuery("select art_coul from abl_art2 group by art_coul order by art_coul")
		self.model23.setQuery(query23)		
		self.ui.comboBox_19.setModel(self.model23)
		self.ui.comboBox_19.setModelColumn(self.model23.fieldIndex("art_coul"))
		self.ui.comboBox_19.setEditable(True)
		self.ui.comboBox_19.setInsertPolicy(0)

		# cbox_meta1
		self.model24 = QtSql.QSqlTableModel()
		query24=QtSql.QSqlQuery("select rcar_id, rcar_lib from "+'"'+"T_STBRCARART"+'"'+" order by rcar_id")
		self.model24.setQuery(query24)		
		self.ui.comboBox_15.setModel(self.model24)
		self.ui.comboBox_15.setModelColumn(self.model24.fieldIndex("rcar_lib"))
		self.ui.comboBox_15.setEditable(True)
		self.ui.comboBox_15.setInsertPolicy(0)

		# cbox_meta11
		self.model25 = QtSql.QSqlTableModel()
		query25=QtSql.QSqlQuery("")
		self.model25.setQuery(query25)
		self.ui.comboBox_23.setModel(self.model25)
		self.ui.comboBox_23.setEditable(True)
		self.ui.comboBox_23.setInsertPolicy(0)

		# cbox_meta2
		self.model26 = QtSql.QSqlTableModel()
		query26=QtSql.QSqlQuery("select rcar_id, rcar_lib from "+'"'+"T_STBRCARART"+'"'+" order by rcar_id")
		self.model26.setQuery(query26)		
		self.ui.comboBox_16.setModel(self.model26)
		self.ui.comboBox_16.setModelColumn(self.model26.fieldIndex("rcar_lib"))
		self.ui.comboBox_16.setEditable(True)
		self.ui.comboBox_16.setInsertPolicy(0)

		# cbox_meta21
		self.model27 = QtSql.QSqlTableModel()
		query27=QtSql.QSqlQuery()
		self.model27.setQuery(query27)
		self.ui.comboBox_24.setModel(self.model27)
		self.ui.comboBox_24.setEditable(True)
		self.ui.comboBox_24.setInsertPolicy(0)

		# cbox_meta3
		self.model28 = QtSql.QSqlTableModel()
		query28=QtSql.QSqlQuery("select rcar_id, rcar_mnemon from "+'"'+"T_STBRCARART"+'"'+" order by rcar_id")
		self.model28.setQuery(query28)		
		self.ui.comboBox_17.setModel(self.model28)
		self.ui.comboBox_17.setModelColumn(self.model28.fieldIndex("rcar_mnemon"))
		self.ui.comboBox_17.setEditable(True)
		self.ui.comboBox_17.setInsertPolicy(0)

		# cbox_meta31
		self.model29 = QtSql.QSqlTableModel()
		query29=QtSql.QSqlQuery()
		self.model29.setQuery(query29)
		self.ui.comboBox_25.setModel(self.model29)
		self.ui.comboBox_25.setEditable(True)
		self.ui.comboBox_25.setInsertPolicy(0)

		#model for line edits
		self.modelLE0 = QtSql.QSqlTableModel()
		self.modelLE1 = QtSql.QSqlTableModel()
		self.modelLE2 = QtSql.QSqlTableModel()

		self.ui.comboBox_7.setEditText("")
		self.ui.comboBox_8.setEditText("")
		self.ui.comboBox_9.setEditText("")
		self.ui.comboBox_10.setEditText("")
		self.ui.comboBox_11.setEditText("")
		self.ui.comboBox_12.setEditText("")
		self.ui.comboBox_13.setEditText("")
		self.ui.comboBox_22.setEditText("")
		self.ui.comboBox_20.setEditText("")
		self.ui.comboBox_14.setEditText("")
		self.ui.comboBox_19.setEditText("")
		self.ui.comboBox_15.setEditText("")
		self.ui.comboBox_23.setEditText("")
		self.ui.comboBox_24.setEditText("")
		self.ui.comboBox_25.setEditText("")
		self.ui.lineEdit.setText("")
		self.ui.lineEdit_2.setText("")

	def connectCBoxes(self):
		self.ui.comboBox.editTextChanged.connect(self._handleC1Change)
		self.ui.comboBox_2.editTextChanged.connect(self._handleC2Change)
		self.ui.comboBox_3.editTextChanged.connect(self._handleC3Change)
		self.ui.comboBox_4.editTextChanged.connect(self._handleC4Change)
		self.ui.comboBox_5.editTextChanged.connect(self._handleC5Change)
		self.ui.comboBox_6.editTextChanged.connect(self._handleC6Change)


	def disconnectCBoxes(self):
		self.ui.comboBox.editTextChanged.disconnect(self._handleC1Change)
		self.ui.comboBox_2.editTextChanged.disconnect(self._handleC2Change)
		self.ui.comboBox_3.editTextChanged.disconnect(self._handleC3Change)
		self.ui.comboBox_4.editTextChanged.disconnect(self._handleC4Change)
		self.ui.comboBox_5.editTextChanged.disconnect(self._handleC5Change)
		self.ui.comboBox_6.editTextChanged.disconnect(self._handleC6Change)


#EVENTS----------------------------------------------------------------------------------------------------------------------
	#TAB1-----------------------------------------------------
	#trigger cbox genus
	def _handleC1Change(self):
		#get cbox_genus id
		a= self.ui.comboBox.currentIndex()
		b= self.ui.comboBox.model().index(a,0)
		c=self.ui.comboBox.model().data(b)
		#change cbox_species content
		query3=QtSql.QSqlQuery("select espece_art from abl_art where guid_fk='" + str(c) + "' group by espece_art order by espece_art")
		self.model3.setQuery(query3)
		self.ui.comboBox_2.clearEditText

		#query4=QtSql.QSqlQuery("WITH RECURSIVE q AS (SELECT  h.*, 1 AS level FROM ott_taxa h WHERE uid = (select guid_fk from abl_art where genre_art ='" + self.ui.comboBox.currentText() + "' group by guid_fk) UNION ALL SELECT  hp.*, level + 1 FROM q JOIN ott_taxa hp ON hp.uid = q.parent_uid) SELECT rank, name, uid FROM q order by level desc")

		#change main_table content
		query=QtSql.QSqlQuery("select code_art, lib1_art, lib2_art, four_art from abl_art where guid_fk='" + str(c) +
			"' order by lib1_art, lib2_art")
		self.model.setQuery(query)
		self.ui.tableView.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)


	#trigger cbox species
	def _handleC2Change(self):
		#get cbox_genus id
		a= self.ui.comboBox.currentIndex()
		b= self.ui.comboBox.model().index(a,0)
		c=self.ui.comboBox.model().data(b)
		#change main_table content
		query=QtSql.QSqlQuery("select code_art, lib1_art, lib2_art, four_art from abl_art where guid_fk='" + str(c) +
			"' and espece_art='" + self.ui.comboBox_2.currentText() + "' order by lib1_art, lib2_art")
		self.model.setQuery(query)



	#trigger cbox family
	def _handleC3Change(self):
		self.disconnectCBoxes()

		#get cbox_family  current id
		a= self.ui.comboBox_3.currentIndex()
		b= self.ui.comboBox_3.model().index(a,0)
		c=self.ui.comboBox_3.model().data(b)

		#change cbox_genus content
		query2=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then upper(q.name)||' ('||q.nb_abl||')' else upper(q.name) end as cgenus from q where q.rank='genus' order by cgenus")
		self.ui.comboBox.model().setQuery(query2)

		#change main_table content
		query=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from q join ott_taxa hc on hc.parent_uid=q.uid) select a.code_art, a.lib1_art, a.lib2_art, a.four_art from abl_art a inner join q on q.uid=a.guid_fk order by a.lib1_art, a.lib2_art")
		self.model.setQuery(query)
		self.ui.tableView.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

		self.connectCBoxes()

	#trigger cbox order
	def _handleC4Change(self):
		self.disconnectCBoxes()
		#get cbox_order  current id
		a= self.ui.comboBox_4.currentIndex()
		b= self.ui.comboBox_4.model().index(a,0)
		c=self.ui.comboBox_4.model().data(b)

		#change family content
		query4=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then q.name||' ('||q.nb_abl||')' else q.name end as cname from q where q.rank='family' order by cname")
		self.ui.comboBox_3.model().setQuery(query4)
		self.ui.comboBox_3.clearEditText

		#change cbox_genus content
		query2=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then upper(q.name)||' ('||q.nb_abl||')' else upper(q.name) end as cgenus from q where q.rank='genus' order by cgenus")
		self.ui.comboBox.model().setQuery(query2)

		#change main_table content
		query=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from q join ott_taxa hc on hc.parent_uid=q.uid) select a.code_art, a.lib1_art, a.lib2_art, a.four_art from abl_art a inner join q on q.uid=a.guid_fk order by a.lib1_art, a.lib2_art")
		self.model.setQuery(query)
		self.ui.tableView.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

		self.connectCBoxes()

	#trigger cbox class
	def _handleC5Change(self):
		self.disconnectCBoxes()
		#get cbox_class  current id
		a= self.ui.comboBox_5.currentIndex()
		b= self.ui.comboBox_5.model().index(a,0)
		c=self.ui.comboBox_5.model().data(b)


		#change order content
		query5=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then q.name||' ('||q.nb_abl||')' else q.name end as cname from q where q.rank='order' order by cname")
		self.ui.comboBox_4.model().setQuery(query5)
		self.ui.comboBox.setModelColumn(self.model5.fieldIndex("cname"))

		#change family content
		query4=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then q.name||' ('||q.nb_abl||')' else q.name end as cname from q where q.rank='family' order by cname")
		self.ui.comboBox_3.model().setQuery(query4)
		self.ui.comboBox.setModelColumn(self.model4.fieldIndex("cname"))

		#change cbox_genus content
		query2=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then upper(q.name)||' ('||q.nb_abl||')' else upper(q.name) end as cgenus from q where q.rank='genus' order by cgenus")
		self.ui.comboBox.model().setQuery(query2)
		self.ui.comboBox.setModelColumn(self.model2.fieldIndex("cgenus"))

		#change main_table content
		query=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from q join ott_taxa hc on hc.parent_uid=q.uid) select a.code_art, a.lib1_art, a.lib2_art, a.four_art from abl_art a inner join q on q.uid=a.guid_fk order by a.lib1_art, a.lib2_art")
		self.model.setQuery(query)
		self.ui.tableView.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

		self.connectCBoxes()

	#trigger cbox phylum
	def _handleC6Change(self):
		self.disconnectCBoxes()
		#get cbox_phylum  current id
		a= self.ui.comboBox_6.currentIndex()
		b= self.ui.comboBox_6.model().index(a,0)
		c=self.ui.comboBox_6.model().data(b)

		#change class content
		query6=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then q.name||' ('||q.nb_abl||')' else q.name end as cname from q where q.rank='class' order by cname")
		self.ui.comboBox_5.model().setQuery(query6)
		self.ui.comboBox.setModelColumn(self.model6.fieldIndex("cname"))
		self.ui.comboBox_5.clearEditText


		#change order content
		query5=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then q.name||' ('||q.nb_abl||')' else q.name end as cname from q where q.rank='order' order by cname")
		self.ui.comboBox_4.model().setQuery(query5)
		self.ui.comboBox.setModelColumn(self.model5.fieldIndex("cname"))

		#change family content
		query4=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then q.name||' ('||q.nb_abl||')' else q.name end as cname from q where q.rank='family' order by cname")
		self.ui.comboBox_3.model().setQuery(query4)
		self.ui.comboBox.setModelColumn(self.model4.fieldIndex("cname"))


		#change cbox_genus content
		query2=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from  q join ott_taxa hc on hc.parent_uid=q.uid) select q.uid, case when q.nb_abl>0 then upper(q.name)||' ('||q.nb_abl||')' else upper(q.name) end as cgenus from q where q.rank='genus' order by cgenus")
		self.ui.comboBox.model().setQuery(query2)
		self.ui.comboBox.setModelColumn(self.model2.fieldIndex("cgenus"))

		#change main_table content
		query=QtSql.QSqlQuery("with recursive q as (select uid, name, rank, nb_abl from ott_taxa h where h.uid='"+str(c)+"' union all select hc.uid, hc.name, hc.rank, hc.nb_abl from q join ott_taxa hc on hc.parent_uid=q.uid) select a.code_art, a.lib1_art, a.lib2_art, a.four_art from abl_art a inner join q on q.uid=a.guid_fk order by a.lib1_art, a.lib2_art")
		self.model.setQuery(query)
		self.ui.tableView.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

		self.connectCBoxes()

	#trigger popup
	def _handleTChange(self):
		a= self.ui.tableView.currentIndex().row()
		b= self.ui.tableView.model().index(a,0)
		c=self.ui.tableView.model().data(b)
		query8=QtSql.QSqlQuery("WITH RECURSIVE q AS (SELECT h.*, 1 as level FROM ott_taxa h WHERE h.uid = (select guid_fk from abl_art where code_art='" + str(c) +"') UNION ALL SELECT hc.*, level+1 FROM q JOIN ott_taxa hc ON hc.uid= q.parent_uid) SELECT  q.rank, q.name FROM q order by level desc")
		self.model8.setQuery(query8)
		self.model8.setHeaderData(0, QtCore.Qt.Horizontal, "Rang")
		self.model8.setHeaderData(1, QtCore.Qt.Horizontal, "Taxon")
		self.ui.tableView_2.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
		self.ui.tableView_2.show()

	#trigger clear tree
	def _handleBChange(self):
		self.disconnectCBoxes()
		self.initData1()
		self.connectCBoxes()

	#TAB2 ------------------------------------------------------------
	#trigger cbox species
	def _handleC7Change(self):
		#get cbox_species  current id
		a= self.ui.comboBox_8.currentIndex()
		b= self.ui.comboBox_8.model().index(a,0)
		c=self.ui.comboBox_8.model().data(b)

		#change variety content
		query14=QtSql.QSqlQuery("with recursive q as (select iuid, i_name, i_rank from "+'"'+"ABL_TAXA"+'"'+" h where h.iuid='"+str(c)+"' union all select hc.iuid, hc.i_name, hc.i_rank from  q join "+'"'+"ABL_TAXA"+'"'+" hc on hc.i_parent_iuid=q.iuid) select q.iuid, q.i_name as cname from q where q.i_rank='Variété' order by cname")
		self.ui.comboBox_9.model().setQuery(query14)
		self.ui.comboBox.setModelColumn(self.model14.fieldIndex("cname"))
		self.ui.comboBox_9.clearEditText

	#trigger cbox meta1
	def _handleC8Change(self):
		#get cbox_meta1  current id
		a= self.ui.comboBox_15.currentIndex()
		b= self.ui.comboBox_15.model().index(a,0)
		c=self.ui.comboBox_15.model().data(b)
		#change meta11 content
		query25=QtSql.QSqlQuery("select c.car_val as cname from "+'"'+"T_STBCARART"+'"'+" c join "+'"'+"T_STBRCARART"+'"'+" r on c.car_id_fk=r.rcar_id where r.rcar_id="+str(c)+" group by cname order by cname")
		self.ui.comboBox_23.model().setQuery(query25)
		self.ui.comboBox.setModelColumn(self.model25.fieldIndex("cname"))
		self.ui.comboBox_23.clearEditText

	#trigger cbox meta2
	def _handleC9Change(self):
		#get cbox_meta2  current id
		a= self.ui.comboBox_16.currentIndex()
		b= self.ui.comboBox_16.model().index(a,0)
		c=self.ui.comboBox_16.model().data(b)
		#change meta31 content
		query27=QtSql.QSqlQuery("select c.car_val as cname from "+'"'+"T_STBCARART"+'"'+" c join "+'"'+"T_STBRCARART"+'"'+" r on c.car_id_fk=r.rcar_id where r.rcar_id="+str(c)+" group by cname order by cname")
		self.ui.comboBox_24.model().setQuery(query27)
		self.ui.comboBox.setModelColumn(self.model27.fieldIndex("cname"))
		self.ui.comboBox_24.clearEditText

	#trigger cbox meta3
	def _handleC10Change(self):
		#get cbox_meta3  current id
		a= self.ui.comboBox_17.currentIndex()
		b= self.ui.comboBox_17.model().index(a,0)
		c=self.ui.comboBox_17.model().data(b)
		#change meta31 content
		query29=QtSql.QSqlQuery("select c.car_val as cname from "+'"'+"T_STBCARART"+'"'+" c join "+'"'+"T_STBRCARART"+'"'+" r on c.car_id_fk=r.rcar_id where r.rcar_id="+str(c)+" group by cname order by cname")
		self.ui.comboBox_25.model().setQuery(query29)
		self.ui.comboBox.setModelColumn(self.model29.fieldIndex("cname"))
		self.ui.comboBox_25.clearEditText

	#trigger update table
	def _handleB2Change(self):
		#string of the query being built on the various comboboxes selected
		s1="select art_code, art_tpot_fk, art_mpot, art_forme_pot, art_four, art_cdtplat, art_hb, art_hh, art_coul, art_forme from abl_art2 a "
		s2="" #for eventual latter outer join metacaracterisation
		s3="where "
		s4=" order by a.art_four, a.art_tpot_fk, a.art_mpot"



		#get current id of taxon selected, browsing up from variety to genus
		self.cb=QtWidgets.QComboBox(self.ui.scrollAreaWidgetContents_2)
		if self.ui.comboBox_9.currentText()!="":
			self.cb=self.ui.comboBox_9
		else:
			if self.ui.comboBox_8.currentText()!="":
				self.cb=self.ui.comboBox_8
			else:
				if self.ui.comboBox_7.currentText()!="":
					self.cb=self.ui.comboBox_7

		a=self.cb.currentIndex()
		b=self.cb.model().index(a,0)
		c=self.cb.model().data(b)
		
		if c:
			s3=s3+"a.art_iuid_fk='"+str(c)+"'"

		#get pot selection
		if self.ui.comboBox_11.currentText():
			a=self.ui.comboBox_11.currentIndex()
			b=self.ui.comboBox_11.model().index(a,0)
			c=self.ui.comboBox_11.model().data(b)

			if len(s3)==6:
				s3=s3+"a.art_tpot_fk='"+str(c)+"'"
			else:
				s3=s3+" and a.art_tpot_fk='"+str(c)+"'"

		if self.ui.comboBox_12.currentText():
			a=self.ui.comboBox_12.currentIndex()
			b=self.ui.comboBox_12.model().index(a,0)
			c=self.ui.comboBox_12.model().data(b)

			if len(s3)==6:
				s3=s3+"a.art_mpot='"+str(c)+"'"
			else:
				s3=s3+" and a.art_mpot='"+str(c)+"'"

		#get cdt selection
		if self.ui.comboBox_13.currentText():
			a=self.ui.comboBox_13.currentIndex()
			b=self.ui.comboBox_13.model().index(a,0)
			c=self.ui.comboBox_13.model().data(b)

			if len(s3)==6:
				s3=s3+"a.art_cdtplat="+str(c)
			else:
				s3=s3+" and a.art_cdtplat="+str(c)

		#get h selection
		if self.ui.comboBox_22.currentText():
			a=self.ui.comboBox_22.currentIndex()
			b=self.ui.comboBox_22.model().index(a,0)
			c=self.ui.comboBox_22.model().data(b)

			if len(s3)==6:
				s3=s3+"a.art_hb="+str(c)
			else:
				s3=s3+" and a.art_hb="+str(c)

		#get mix selection
		if self.ui.comboBox_20.currentText():
			a=self.ui.comboBox_20.currentIndex()
			b=self.ui.comboBox_20.model().index(a,0)
			c=self.ui.comboBox_20.model().data(b)

			if len(s3)==6:
				s3=s3+"a.art_mix='"+str(c)+"'"
			else:
				s3=s3+" and a.art_mix='"+str(c)+"'"

		#get four selection
		if self.ui.comboBox_10.currentText():
			a=self.ui.comboBox_10.currentIndex()
			b=self.ui.comboBox_10.model().index(a,0)
			c=self.ui.comboBox_10.model().data(b)

			if len(s3)==6:
				s3=s3+"a.art_four='"+str(c)+"'"
			else:
				s3=s3+" and a.art_four='"+str(c)+"'"

		#get coul selection
		if self.ui.comboBox_19.currentText():
			a=self.ui.comboBox_19.currentIndex()
			b=self.ui.comboBox_19.model().index(a,0)
			c=self.ui.comboBox_19.model().data(b)

			if len(s3)==6:
				s3=s3+"a.art_coul='"+str(c)+"'"
			else:
				s3=s3+" and a.art_coul='"+str(c)+"'"

		#get forme selection
		if self.ui.comboBox_14.currentText():
			a=self.ui.comboBox_14.currentIndex()
			b=self.ui.comboBox_14.model().index(a,0)
			c=self.ui.comboBox_14.model().data(b)

			if len(s3)==6:
				s3=s3+"a.art_forme='"+str(c)+"'"
			else:
				s3=s3+" and a.art_forme='"+str(c)+"'"


		#get first meta selection
		if self.ui.comboBox_15.currentText() and self.ui.comboBox_23.currentText():
			a=self.ui.comboBox_15.currentIndex()
			b=self.ui.comboBox_15.model().index(a,0)
			c=self.ui.comboBox_15.model().data(b)
			d=self.ui.comboBox_23.currentIndex()
			e=self.ui.comboBox_23.model().index(d,0)
			f=self.ui.comboBox_23.model().data(e)

			s2="full join "+'"'+"T_STBCARART"+'"'+" c on c.car_code_art_fk=a.art_code "
			if len(s3)==6:
				s3=s3+"c.car_id_fk="+str(c)+" and c.car_val='"+str(f)+"'"
			else:
				s3=s3+" and c.car_id_fk="+str(c)+" and c.car_val='"+str(f)+"'"

		#get second meta selection
		if self.ui.comboBox_16.currentText() and self.ui.comboBox_24.currentText():
			a=self.ui.comboBox_16.currentIndex()
			b=self.ui.comboBox_16.model().index(a,0)
			c=self.ui.comboBox_16.model().data(b)
			d=self.ui.comboBox_24.currentIndex()
			e=self.ui.comboBox_24.model().index(d,0)
			f=self.ui.comboBox_24.model().data(e)

			s2=s2+" full join "+'"'+"T_STBCARART"+'"'+" c2 on c2.car_code_art_fk=a.art_code "
			if len(s3)==6:
				s3=s3+"c2.car_id_fk="+str(c)+" and c2.car_val='"+str(f)+"'"
			else:
				s3=s3+" and c2.car_id_fk="+str(c)+" and c2.car_val='"+str(f)+"'"

		if len(s3)!=6:
			s=s1+s2+s3+s4
		else:
			s=s1+s4
		query11=QtSql.QSqlQuery(s)
		self.model11.setQuery(query11)

	#trigger line edits for full name reconstruction at bottom
	def _handleT2Change(self):
		lib1=""
		lib2=""
		#get article code
		a= self.ui.tableView_3.currentIndex().row()
		b= self.ui.tableView_3.model().index(a,0)
		c= self.ui.tableView_3.model().data(b)

		#queries to get botanic triad
		queryLE0= QtSql.QSqlQuery("SELECT iuid, i_name, i_rank FROM "+'"'+"ABL_TAXA"+'"'+" h WHERE h.iuid = (select art_iuid_fk from abl_art2 where art_code='" + str(c) +"')")
		self.modelLE0.setQuery(queryLE0)
		bB=self.modelLE0.data(self.modelLE0.index(0,0))
		bN=self.modelLE0.data(self.modelLE0.index(0,1))
		bR=self.modelLE0.data(self.modelLE0.index(0,2))

		if bR=='Variété':
			queryLE1=QtSql.QSqlQuery("WITH RECURSIVE q AS (SELECT h.*, 1 as level FROM "+'"'+"ABL_TAXA"+'"'+" h WHERE h.iuid = (select art_iuid_fk from abl_art2 where art_code='" + str(c) +"') UNION ALL SELECT hc.*, level+1 FROM q JOIN "+'"'+"ABL_TAXA"+'"'+" hc ON hc.iuid= q.i_parent_iuid) SELECT q.i_name FROM q order by level desc")
			self.modelLE1.setQuery(queryLE1)
			b1N=self.modelLE1.data(self.modelLE1.index(1,0))
			b2N=self.modelLE1.data(self.modelLE1.index(0,0))
			lib1=b2N+" "+b1N
			lib2="'"+bN+"'"
		else:
			if bR=='espèce':
				queryLE1=QtSql.QSqlQuery("WITH RECURSIVE q AS (SELECT h.*, 1 as level FROM "+'"'+"ABL_TAXA"+'"'+" h WHERE h.iuid = (select art_iuid_fk from abl_art2 where art_code='" + str(c) +"') UNION ALL SELECT hc.*, level+1 FROM q JOIN "+'"'+"ABL_TAXA"+'"'+" hc ON hc.iuid= q.i_parent_iuid) SELECT q.i_name FROM q where q.i_rank='GENRE'")
				self.modelLE1.setQuery(queryLE1)
				b1N=self.modelLE1.data(self.modelLE1.index(0,0))
				lib1=b1N + " " + bN
			else:
				lib1=bN

		#queries to get general data about article
		queryLE1=QtSql.QSqlQuery("select art_tpot_fk, art_mpot, art_forme_pot, art_cdtplat, art_hb, art_hh, art_coul, art_forme from abl_art2 where art_code='"+str(c)+"'")
		self.modelLE1.setQuery(queryLE1)
		aT=self.modelLE1.data(self.modelLE1.index(0,0))
		aM=self.modelLE1.data(self.modelLE1.index(0,1))
		aFP=self.modelLE1.data(self.modelLE1.index(0,2))
		aCD=self.modelLE1.data(self.modelLE1.index(0,3))
		aHB=self.modelLE1.data(self.modelLE1.index(0,4))
		aHH=self.modelLE1.data(self.modelLE1.index(0,5))
		aC=self.modelLE1.data(self.modelLE1.index(0,6))
		aF=self.modelLE1.data(self.modelLE1.index(0,7))

		if aM:
			lib1=lib1+" "+str(aT or "")+str(aM or "")+" "+str(aFP or "")

		if aHB and aHH and (not(aCD) or aCD==1):
			lib2=lib2+" "+str(aHB or "")+"-"+str(aHH or "")+"cm "+str(aC or "")+" "+str(aF or "")
		elif aHB and aHH and aCD>1:
			lib2="x"+str(aCD or "")+" "+lib2+" "+str(aHB or "")+"-"+str(aHH or "")+"cm "+str(aC or "")+" "+str(aF or "")
		elif aHB and not(aHH) and (not(aCD) or aCD==1):
			lib2=lib2+" "+str(aHB or "")+"cm "+str(aC or "")+" "+str(aF or "")
		elif aHB and not(aHH) and aCD>1:
			lib2="x"+str(aCD or "")+" "+lib2+" "+str(aHB or "")+"cm "+str(aC or "")+" "+str(aF or "")
		elif not(aHB) and not(aHH) and (not(aCD) or aCD==1):
			lib2=lib2+" "+str(aC or "")+" "+str(aF or "")
		elif not(aHB) and not(aHH) and aCD>1:
			lib2="x"+str(aCD or "")+" "+lib2+" "+str(aC or "")+" "+str(aF or "")

		if aM=='05' or aM=='06':
			lib1="MINI "+lib1

		#queries to get metadata
		queryLE2= QtSql.QSqlQuery("SELECT count(*) FROM "+'"'+"T_STBCARART"+'"'+" WHERE car_code_art_fk ='" + str(c) +"'")
		self.modelLE2.setQuery(queryLE2)
		mC=self.modelLE2.data(self.modelLE2.index(0,0))
		queryLE2= QtSql.QSqlQuery("select r.rcar_mnemon, c.car_val from "+'"'+"T_STBCARART"+'"'+" c join "+'"'+"T_STBRCARART"+'"'+" r on r.rcar_id=c.car_id_fk where c.car_code_art_fk ='" + str(c) +"' order by r.rcar_mnemon")
		self.modelLE2.setQuery(queryLE2)

		if mC==1:
			mH=self.modelLE2.data(self.modelLE2.index(0,0))
			mV=self.modelLE2.data(self.modelLE2.index(0,1))
			lib2=lib2+" "+mV+mH
		elif mC==2:
			mH=self.modelLE2.data(self.modelLE2.index(0,0))
			mV=self.modelLE2.data(self.modelLE2.index(0,1))
			m2H=self.modelLE2.data(self.modelLE2.index(1,0))
			m2V=self.modelLE2.data(self.modelLE2.index(1,1))
			lib2=lib2+" "+mV+mH+" "+m2V+m2H

		lib1=" ".join(lib1.split())
		lib2=" ".join(lib2.split())
		self.ui.lineEdit.setText(lib1)
		self.ui.lineEdit_2.setText(lib2)


	#trigger clear tab 2
	def _handleB3Change(self):
		self.initData2()



	#key press

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			self.ui.tableView_2.hide()





#CUSTOM CLASS & MAIN----------------------------------------------------------------------------------------------------------------------------------		    
class CustomSqlModel(QtSql.QSqlTableModel):
	def __init__(self, parent=None):
		QtSql.QSqlTableModel.__init__(self, parent=parent)
	def data(self, index, role):
		if role == QtCore.Qt.BackgroundRole:
			if index.row() in [2, 4]:
				return QtGui.QBrush(QtCore.Qt.yellow)
		return QtSql.QSqlTableModel.data(self, index, role)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)	
	#print (QtWidgets.QStyleFactory.keys())
	app.setStyle("Fusion")
	myapp = R_Phylo()
	myapp.show()
	sys.exit(app.exec_())


#bordel
