#https://leetcode.com/problems/unique-email-addresses/
class Solution(object):

    def transform_email(self, email):

        local, domain = email.split("@")
        plus_index=local.index("+")
        local = local[:plus_index]
        local=local.replace(".","")
        email = "".join([local,"@",domain])

        return email

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            email_set.add(self.transform_email(email))
        return len(email_set)



s = Solution()
s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])


