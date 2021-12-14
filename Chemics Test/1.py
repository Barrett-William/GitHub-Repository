import chemics as cm

ce = cm.ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')

print(ce.balance)
# returns True for balanced equation
ce2 = cm.ChemicalEquation('C4H8 + 6 02 -> 4 CO2 + 4 H20')
print(ce2.balance)

print(ce.rct_properties)
# returns a dataframe of the reactant properties
#                HCl        Na
# moles            2         2
# species        HCl        Na
# molwt       36.458     22.99
# mass        72.916     45.98
# molfrac        0.5       0.5
# massfrac  0.613275  0.386725