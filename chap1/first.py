# -*- coding: utf-8 -*-

import survey

table = survey.Pregnancies()
table.ReadRecords()
print u'妊娠レコード総数:', len(table.records)
