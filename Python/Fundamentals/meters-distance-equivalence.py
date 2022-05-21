meters = float(input('Type the distance in meters to check it equivalences:'))
km = meters/1000
hm = meters/100
dam = meters/10
dm = meters*10
cm = meters*100
mm = meters*1000
print(
    f'The distance of {meters}m is equals to:\n{km:.3f}km\n{hm:.2f}hm\n{dam:.1f}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm\n')
