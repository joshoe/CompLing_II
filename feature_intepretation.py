

# idx:  0       1                       2               3           4       5           6
# post: [userid,subreddit,              totw,           totmissp,   tot1sg, totpron,    totpres,
#
# ...   7       8 - 25                   26             27          28      29          30
# ...   totvrb, [funcwrdcts and liwc],  [topicSpaceVec],wkday,      hr,     timestamp,  label]



















def interpretFeatures(post, dicSub2TopVec, mentalHealthVec):
	'''
	:param post: a list of features
	:param dicSub2TopVec:
	:param mentalHealthVec:
	:return: interpretted_post: a list of updated features
	'''
