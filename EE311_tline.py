import cmath 

def getGamma_L(ZL, ZO):
    return (ZL-ZO) / (ZL+ZO)

def getGamma_in(GL, L):
    exponent = cmath.exp(1j*2*2*cmath.pi*L)
    return GL * exponent

def getZ_in(Gin, Zo):
    return Zo * (1+Gin) / (1-Gin)

def getVnx_fromVpx(gamma_x, Vpx):
    return gamma_x * Vpx

def getVpx_fromVnx(gamma_x, Vnx):
    return gamma_x / Vnx

def getVpnx_fromVpnL(VpnL, L, vpos: bool):
    if vpos: scalar = -1 
    else: scalar = 1 
    exponent = cmath.exp(1j*2*cmath.pi*L*scalar)
    return VpnL * exponent 

def getVpnL_fromVpnx(Vpnx, L, vpos: bool):
    if vpos: scalar = -1 
    else: scalar = 1 
    exponent = cmath.exp(1j*2*cmath.pi*L*scalar)
    return Vpnx / exponent 

def getIpx(Vpx, Zo):
    return Vpx / Zo

def getInx(Vnx, Zo):
    return -Vnx / Zo

def getIx(Ipx, Inx):
    return Ipx + Inx

def getVx(Vpx, Vnx):
    return Vpx + Vnx

def getAvgPower(V, I):
    return 0.5 * V * I.conjugate()

def main():
    # Define parameters given or not given
    # -- Resistances --
    Zl = None
    Zg = None
    Zo = None
    # -- Voltages --
    V = None
    Vp_in = None
    Vn_in = None
    VpL = None
    VnL = None
    # -- Currents --
    I = None
    Ip_in = None
    In_in = None
    IpL = None
    InL = None
    # -- Characteristics --
    length = None
    gamma_L = None
    gamma_in = None

    if (gamma_L is None and Zl is not None and Zo is not None):
        gamma_L = getGamma_L(Zl, Zo)
    if (length is not None):
        gamma_in = getGamma_in(gamma_L, length)
    

if __name__ == "__main__":
    main()