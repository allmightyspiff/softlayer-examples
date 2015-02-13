import SoftLayer
import sys
import pprint


pp = pprint.PrettyPrinter(indent=4)
client = SoftLayer.Client(username=apiUsername,api_key=apiKey)
obj=client['SoftLayer_Account'].getNextInvoiceTotalAmount()

pp.pprint(obj)

print "\033[31mNEXT\033[0m"
items = ['nextInvoiceTotalAmount',
         'nextInvoiceTotalRecurringAmount',
         'nextInvoiceTotalRecurringTaxAmount',
         'nextInvoiceTotalOneTimeAmount',
         'nextInvoiceTotalOneTimeTaxAmount',
         'nextInvoiceTopLevelBillingItems[children,nextInvoiceTotalRecurringAmount,nextInvoiceTotalRecurringTaxAmount,nextInvoiceTotalOneTimeAmount,nextInvoiceTotalOneTimeTaxAmount]'
]

items1 = ['allTopLevelBillingItemCount','allTopLevelBillingItems']

Omask = "mask[%s]" % ','.join(items1)

pp.pprint(Omask)


obj = client['SoftLayer_Account'].getObject(mask=Omask)
pp.pprint(obj)
