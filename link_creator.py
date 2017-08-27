#really simple code to generate links to scrap data from web in parallel using hadoop
#getting data from github

f = open('github_links.txt','w')

link = 'https://github.com/search?l=Python&p={}&q=python&type=Repositories&utf8=%E2%9C%93\n'
for n in range(1,101):
    f.write(link.format(n))

f.close()
