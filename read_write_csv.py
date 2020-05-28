from Retailer.views import RetailerImage
import csv
with open("/home/suraj/Documents/surajretailimage.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]

for item in data_read[1::]:
    RetailerImage.objects.filter(category=item[3],brand_name=item[1]).update(brand_logo=item[2])

