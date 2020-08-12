import requests


class WebScrap:
    def getQuote(url):
        res = requests.get(url)
        temp_strp = res.text
        strt_indx = temp_strp.find('<span class="txt15B nse_span_price_wrap')
        end_indx = temp_strp.find('</span>',strt_indx)
        str1 = temp_strp[strt_indx:end_indx+7:]
        strt_indx1 = str1.find('>')
        end_indx1 = str1.find('<',strt_indx1)
        str2 = str1[strt_indx1+1:end_indx1:]
        return float(str2)
