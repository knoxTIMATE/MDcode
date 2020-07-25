def Calculate_temperature(vel, BoxSize, DIM, N):
    ene_kin=0.0

    for i in range(N):
        real_vel=BoxSize*vel[i:]
        ene_kin = ene_kin + 0.5*np.dot(real_vel, real_vel)
    ene_kin_aver=1.0*ene_kin/N
    temperature = 2.0*ene_kin_aver/DIM

    return ene_kin_aver, temperature

