# SET_BIT implementation
def SET_BIT(VAR, BITNO):
    VAR |= (1 << BITNO)
    return VAR

# CLR_BIT implementation
def CLR_BIT(VAR, BITNO):
    VAR &= ~(1 << BITNO)
    return VAR

# TOG_BIT implementation
def TOG_BIT(VAR, BITNO):
    VAR ^= (1 << BITNO)
    return VAR

# GET_BIT implementation
def GET_BIT(VAR, BITNO):
    return (VAR >> BITNO) & 1