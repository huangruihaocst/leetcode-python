class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = dict()
        for cpdomain in cpdomains:
            times = int(cpdomain.split(' ')[0])
            domain = cpdomain.split(' ')[1]
            domains = domain.split('.')
            for i in range(0, len(domains)):
                subdomain = '.'.join(domains[i:])
                if subdomain in d:
                    d[subdomain] += times
                else:
                    d[subdomain] = times
        res = list()
        for domain in d:
            res.append(str(d[domain]) + ' ' + domain)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
