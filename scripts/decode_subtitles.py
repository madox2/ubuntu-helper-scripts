#!/usr/bin/python
import sys
import urllib

source_enc = 'windows-1250'
target_enc = 'utf-8'

print '============================================='
print '=== conversion from windows-1250 to utf-8 ==='
print '============================================='

print '-> processing arguments'
argv = iter(sys.argv)
next(argv)

for arg in argv:
	try:
		filename = str(arg)
		print '-> processing file ' + filename
		# prepare user input
		filename = urllib.unquote(filename).decode('utf-8').strip()
		if filename.startswith('file://'):
			filename = filename[7:]

		print '-> opening file for reading'
		f = open(filename)
		content = f.read()
		f.close()

		print '-> opening file for writing'
		f = open(filename, 'w')
		print '-> encoding file'
		f.write(unicode(content, source_enc).encode(target_enc))
		f.close()

		print '============================================='
		print '================= SUCCESS ==================='
		print '============================================='
	except Exception as e:
		print '============================================='
		print '================== FAIL ====================='
		print e.__doc__
		print '============================================='
