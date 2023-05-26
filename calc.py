
#сумма, процент, период(года)
def anyitent(summS, percent_yearS, periodS):
    
  try:
    summ = int(summS)
    percent_year = int(percent_yearS)
    period = int(periodS)
    
    if summ <= 0 or percent_year<=0 or period <=0:
      return "Так не бывает, давай по новой"
    
    percent_month = percent_year / 1200.0
    month = period * 12.0
    k = (percent_month * pow(1 + percent_month, month)) / (pow(1 + percent_month, month) - 1)
    
    return round(summ * k, 2)
  
  
  except ValueError:
    pass

#сумма, процент, период(года)
def deff(summS, percent_yearsS, nS):
  try:
    summ = int(summS)
    percent_years = int(percent_yearsS)
    n = int(nS)
    
    month = n * 12
    month_percent = percent_years / (12 * 100)
    first_pay = summ / month
    
    month_pay = []
    SUM = 0
    for i in range(1, month + 1):
      month_pay.append(str(round(first_pay + (summ - (first_pay * (i - 1))) * month_percent,1)) + ' ')  
      SUM += round(first_pay + (summ - (first_pay * (i - 1))) * month_percent,1)
    month_pay.append('Полная сумма всех выплат: '+ str(SUM))
    return month_pay
  except ValueError:
    pass