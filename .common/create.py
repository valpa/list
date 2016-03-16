import sys
import csv

inf = sys.argv[1]
src = '../.common/template.htm'
dst = inf.split('.')[0]+'.htm'

with open(src) as f:
    mlines = f.read().splitlines()

dpN = 0
mdpN = 0

with open(inf, 'rb') as f:
	for line in f:
		line = line.rstrip()
		if not line: continue
		if line.startswith("#"): continue
		if line.startswith(" "): continue
		k = line.split('=')[0]
		v = line.split('=')[1]
			
		if k in ['Title', 'TitleIconPic', 'FeatureList', 'SpecificationList']:
			g = [ i for i, word in enumerate(mlines) if word.startswith('<!--'+k) ]
			if g:
				mm = mlines[ g[0] ][len('<!--'+k):][:-3]
				mlines.insert( g[0], mm.replace(k,v) )

		if k in [ 'DetailPic', 'MoreDetailPic', 'DescriptionText', 'SpecialTCText' ]:
			try:
				mlines.remove('<!--'+k+'Off')
				mlines.remove(k+'Off'+'-->')
				g = [ i for i, word in enumerate(mlines) if word.startswith('<!--'+k) ]
				print 'find ' + '<!--' + k +':   '+ str	(g)
				print ' - to add --> in end'
				if g:
					mlines[ g[0] ] = mlines[ g[0] ] + '-->'
			except:
				pass
				
			g = [ i for i, word in enumerate(mlines) if word.startswith('<!--'+k) ]
			print 'find ' + '<!--' + k +':   '+ str	(g)
			print ' - to remove comment, and replace the key' 
			if g:
				mm = mlines[ g[0] ][len('<!--'+k):][:-3]
				mlines.insert( g[0], mm.replace(k,v) )
			
			g = [ i for i, word in enumerate(mlines) if 'X'+k+'0' in word ]
			print 'find ' + 'X'+ k+'0' +':   '+ str(g)
			print ' - to replace' 
			if g:
				mlines[ g[0] ] = mlines[ g[0] ].replace('X'+k+'0',v)
				
				

with open(dst, 'w') as f:
	f.write( '\n'.join(mlines) )
	
print 'done'