import re

def grabUrls(text):
    """Given a text string, returns all the urls we can find in it."""
    return url_re.findall(text)

# ! added https 
urls = '(?: %s)' % '|'.join("""http https telnet gopher file wais
ftp""".split())
ltrs = r'\w'
gunk = r'/#~:.?+=&%@!\-'
punc = r'.:?\-'
any = "%(ltrs)s%(gunk)s%(punc)s" % { 'ltrs' : ltrs,
                                     'gunk' : gunk,
                                     'punc' : punc }

url = r"""
    \b                            # start at word boundary
        %(urls)s    :             # need resource and a colon
        [%(any)s]  +?             # followed by one or more
                                  #  of any valid character, but
                                  #  be conservative and take only
                                  #  what you need to....
    (?=                           # look-ahead non-consumptive assertion
            [%(punc)s]*           # either 0 or more punctuation
            (?:   [^%(any)s]      #  followed by a non-url char
                |                 #   or end of the string
                  $
            )
    )
    """ % {'urls' : urls,
           'any' : any,
           'punc' : punc }

url_re = re.compile(url, re.VERBOSE | re.MULTILINE)


def _test():
    # sample = """hello world, this is an url:
    #             http://python.org.  Can you find it?"""

    sample = """<h1 itemprop="headline" class="article-card-title">            <a href="https://www.makeuseof.com/tag/best-usb-fingerprint-scanners/">\n              The 6 Best USB Fingerprint Scanners for PCs and Laptops            </a>\n          </h1>"""
    match = url_re.search(sample)
    print ("Here's what we found: '%s'" % match.group(0))

if __name__ == '__main__':
    _test()
    #p = """<h1 itemprop="headline" class="article-card-title">\n            <a href="https://www.makeuseof.com/tag/best-iptv-box/">\n              The Best IPTV Set Top Boxes in 2019            </a>\n          </h1>', '<h1 itemprop="headline" class="article-card-title">\n            <a href="https://www.makeuseof.com/tag/best-computer-for-music-production/">\n              The 8 Best Computers for Music Production            </a>\n          </h1>', '<h1 itemprop="headline" class="article-card-title">\n            <a href="https://www.makeuseof.com/tag/best-ddr4-ram/">\n              The Best DDR4 RAM to Improve Your PC’s Performance            </a>\n          </h1>', '<h1 itemprop="headline" class="article-card-title">\n            <a href="https://www.makeuseof.com/tag/best-vertical-mice/">\n              The 7 Best Ergonomic Vertical Mice            </a>\n          </h1>', '<h1 itemprop="headline" class="article-card-title">\n            <a href="https://www.makeuseof.com/tag/best-cheap-smartwatch/">\n              The 6 Best Cheap Smartwatches for Fitness and Notifications            </a>\n          </h1>', '<h1 itemprop="headline" class="article-card-title">\n            <a href="https://www.makeuseof.com/tag/best"""
    #print(grabUrls(p))
###