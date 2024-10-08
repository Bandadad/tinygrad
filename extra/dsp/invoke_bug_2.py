from tinygrad.runtime.ops_dsp import DSPDevice

kernel = """__attribute__((noinline)) void r_64_4_4_64_4_4_4(float* restrict __attribute__((align_value(128))) data0, const float* restrict __attribute__((align_value(128))) data1, const float* restrict __attribute__((align_value(128))) data2, const float* restrict __attribute__((align_value(128))) data3) {
  for (int ridx0 = 0; ridx0 < 64; ridx0++) {
    int alu0 = (ridx0*4096);
    for (int ridx1 = 0; ridx1 < 4; ridx1++) {
      int alu1 = (ridx1*64);
      for (int ridx2 = 0; ridx2 < 4; ridx2++) {
        int alu2 = (ridx2*4);
        int alu3 = ((ridx0*1024)+alu1+alu2);
        int alu4 = (alu1+alu2);
        float val0 = data3[alu4+1];
        float val1 = data3[alu4+2];
        float val2 = data3[alu4+3];
        float val3 = data3[alu4+16];
        float val4 = data3[alu4+17];
        float val5 = data3[alu4+18];
        float val6 = data3[alu4+19];
        float val7 = data3[alu4+32];
        float val8 = data3[alu4+33];
        float val9 = data3[alu4+34];
        float val10 = data3[alu4+35];
        float val11 = data3[alu4+48];
        float val12 = data3[alu4+49];
        float val13 = data3[alu4+50];
        float val14 = data3[alu4+51];
        float val15 = data3[alu4];
        float acc0 = 0.0f;
        float acc1 = 0.0f;
        float acc2 = 0.0f;
        float acc3 = 0.0f;
        float acc4 = 0.0f;
        float acc5 = 0.0f;
        float acc6 = 0.0f;
        float acc7 = 0.0f;
        float acc8 = 0.0f;
        float acc9 = 0.0f;
        float acc10 = 0.0f;
        float acc11 = 0.0f;
        float acc12 = 0.0f;
        float acc13 = 0.0f;
        float acc14 = 0.0f;
        float acc15 = 0.0f;
        float acc16 = 0.0f;
        float acc17 = 0.0f;
        float acc18 = 0.0f;
        float acc19 = 0.0f;
        float acc20 = 0.0f;
        float acc21 = 0.0f;
        float acc22 = 0.0f;
        float acc23 = 0.0f;
        float acc24 = 0.0f;
        float acc25 = 0.0f;
        float acc26 = 0.0f;
        float acc27 = 0.0f;
        float acc28 = 0.0f;
        float acc29 = 0.0f;
        float acc30 = 0.0f;
        float acc31 = 0.0f;
        float acc32 = 0.0f;
        float acc33 = 0.0f;
        float acc34 = 0.0f;
        float acc35 = 0.0f;
        float acc36 = 0.0f;
        float acc37 = 0.0f;
        float acc38 = 0.0f;
        float acc39 = 0.0f;
        float acc40 = 0.0f;
        float acc41 = 0.0f;
        float acc42 = 0.0f;
        float acc43 = 0.0f;
        float acc44 = 0.0f;
        float acc45 = 0.0f;
        float acc46 = 0.0f;
        float acc47 = 0.0f;
        float acc48 = 0.0f;
        float acc49 = 0.0f;
        float acc50 = 0.0f;
        float acc51 = 0.0f;
        float acc52 = 0.0f;
        float acc53 = 0.0f;
        float acc54 = 0.0f;
        float acc55 = 0.0f;
        float acc56 = 0.0f;
        float acc57 = 0.0f;
        float acc58 = 0.0f;
        float acc59 = 0.0f;
        float acc60 = 0.0f;
        float acc61 = 0.0f;
        float acc62 = 0.0f;
        float acc63 = 0.0f;
        for (int ridx3 = 0; ridx3 < 64; ridx3++) {
          int alu5 = (alu0+(ridx2*256)+ridx3);
          float val16 = data2[alu5+64];
          float val17 = data2[alu5+128];
          float val18 = data2[alu5+192];
          float val19 = data2[alu5+1024];
          float val20 = data2[alu5+1088];
          float val21 = data2[alu5+1152];
          float val22 = data2[alu5+1216];
          float val23 = data2[alu5+2048];
          float val24 = data2[alu5+2112];
          float val25 = data2[alu5+2176];
          float val26 = data2[alu5+2240];
          float val27 = data2[alu5+3072];
          float val28 = data2[alu5+3136];
          float val29 = data2[alu5+3200];
          float val30 = data2[alu5+3264];
          float val31 = data2[alu5];
          int alu6 = (alu0+(ridx1*256)+ridx3);
          float val32 = data1[alu6+64];
          float val33 = data1[alu6+128];
          float val34 = data1[alu6+192];
          float val35 = data1[alu6+1024];
          float val36 = data1[alu6+1088];
          float val37 = data1[alu6+1152];
          float val38 = data1[alu6+1216];
          float val39 = data1[alu6+2048];
          float val40 = data1[alu6+2112];
          float val41 = data1[alu6+2176];
          float val42 = data1[alu6+2240];
          float val43 = data1[alu6+3072];
          float val44 = data1[alu6+3136];
          float val45 = data1[alu6+3200];
          float val46 = data1[alu6+3264];
          float val47 = data1[alu6];
          acc0 = (acc0+(val47*val31));
          acc1 = (acc1+(val35*val19));
          acc2 = (acc2+(val39*val23));
          acc3 = (acc3+(val43*val27));
          acc4 = (acc4+(val32*val31));
          acc5 = (acc5+(val36*val19));
          acc6 = (acc6+(val40*val23));
          acc7 = (acc7+(val44*val27));
          acc8 = (acc8+(val33*val31));
          acc9 = (acc9+(val37*val19));
          acc10 = (acc10+(val41*val23));
          acc11 = (acc11+(val45*val27));
          acc12 = (acc12+(val34*val31));
          acc13 = (acc13+(val38*val19));
          acc14 = (acc14+(val42*val23));
          acc15 = (acc15+(val46*val27));
          acc16 = (acc16+(val47*val16));
          acc17 = (acc17+(val35*val20));
          acc18 = (acc18+(val39*val24));
          acc19 = (acc19+(val43*val28));
          acc20 = (acc20+(val32*val16));
          acc21 = (acc21+(val36*val20));
          acc22 = (acc22+(val40*val24));
          acc23 = (acc23+(val44*val28));
          acc24 = (acc24+(val33*val16));
          acc25 = (acc25+(val37*val20));
          acc26 = (acc26+(val41*val24));
          acc27 = (acc27+(val45*val28));
          acc28 = (acc28+(val34*val16));
          acc29 = (acc29+(val38*val20));
          acc30 = (acc30+(val42*val24));
          acc31 = (acc31+(val46*val28));
          acc32 = (acc32+(val47*val17));
          acc33 = (acc33+(val35*val21));
          acc34 = (acc34+(val39*val25));
          acc35 = (acc35+(val43*val29));
          acc36 = (acc36+(val32*val17));
          acc37 = (acc37+(val36*val21));
          acc38 = (acc38+(val40*val25));
          acc39 = (acc39+(val44*val29));
          acc40 = (acc40+(val33*val17));
          acc41 = (acc41+(val37*val21));
          acc42 = (acc42+(val41*val25));
          acc43 = (acc43+(val45*val29));
          acc44 = (acc44+(val34*val17));
          acc45 = (acc45+(val38*val21));
          acc46 = (acc46+(val42*val25));
          acc47 = (acc47+(val46*val29));
          acc48 = (acc48+(val47*val18));
          acc49 = (acc49+(val35*val22));
          acc50 = (acc50+(val39*val26));
          acc51 = (acc51+(val43*val30));
          acc52 = (acc52+(val32*val18));
          acc53 = (acc53+(val36*val22));
          acc54 = (acc54+(val40*val26));
          acc55 = (acc55+(val44*val30));
          acc56 = (acc56+(val33*val18));
          acc57 = (acc57+(val37*val22));
          acc58 = (acc58+(val41*val26));
          acc59 = (acc59+(val45*val30));
          acc60 = (acc60+(val34*val18));
          acc61 = (acc61+(val38*val22));
          acc62 = (acc62+(val42*val26));
          acc63 = (acc63+(val46*val30));
        }
        data0[alu3] = ((acc0*0.125f)+val15);
        data0[alu3+256] = ((acc1*0.125f)+val15);
        data0[alu3+512] = ((acc2*0.125f)+val15);
        data0[alu3+768] = ((acc3*0.125f)+val15);
        data0[alu3+16] = ((acc4*0.125f)+val3);
        data0[alu3+272] = ((acc5*0.125f)+val3);
        data0[alu3+528] = ((acc6*0.125f)+val3);
        data0[alu3+784] = ((acc7*0.125f)+val3);
        data0[alu3+32] = ((acc8*0.125f)+val7);
        data0[alu3+288] = ((acc9*0.125f)+val7);
        data0[alu3+544] = ((acc10*0.125f)+val7);
        data0[alu3+800] = ((acc11*0.125f)+val7);
        data0[alu3+48] = ((acc12*0.125f)+val11);
        data0[alu3+304] = ((acc13*0.125f)+val11);
        data0[alu3+560] = ((acc14*0.125f)+val11);
        data0[alu3+816] = ((acc15*0.125f)+val11);
        data0[alu3+1] = ((acc16*0.125f)+val0);
        data0[alu3+257] = ((acc17*0.125f)+val0);
        data0[alu3+513] = ((acc18*0.125f)+val0);
        data0[alu3+769] = ((acc19*0.125f)+val0);
        data0[alu3+17] = ((acc20*0.125f)+val4);
        data0[alu3+273] = ((acc21*0.125f)+val4);
        data0[alu3+529] = ((acc22*0.125f)+val4);
        data0[alu3+785] = ((acc23*0.125f)+val4);
        data0[alu3+33] = ((acc24*0.125f)+val8);
        data0[alu3+289] = ((acc25*0.125f)+val8);
        data0[alu3+545] = ((acc26*0.125f)+val8);
        data0[alu3+801] = ((acc27*0.125f)+val8);
        data0[alu3+49] = ((acc28*0.125f)+val12);
        data0[alu3+305] = ((acc29*0.125f)+val12);
        data0[alu3+561] = ((acc30*0.125f)+val12);
        data0[alu3+817] = ((acc31*0.125f)+val12);
        data0[alu3+2] = ((acc32*0.125f)+val1);
        data0[alu3+258] = ((acc33*0.125f)+val1);
        data0[alu3+514] = ((acc34*0.125f)+val1);
        data0[alu3+770] = ((acc35*0.125f)+val1);
        data0[alu3+18] = ((acc36*0.125f)+val5);
        data0[alu3+274] = ((acc37*0.125f)+val5);
        data0[alu3+530] = ((acc38*0.125f)+val5);
        data0[alu3+786] = ((acc39*0.125f)+val5);
        data0[alu3+34] = ((acc40*0.125f)+val9);
        data0[alu3+290] = ((acc41*0.125f)+val9);
        data0[alu3+546] = ((acc42*0.125f)+val9);
        data0[alu3+802] = ((acc43*0.125f)+val9);
        data0[alu3+50] = ((acc44*0.125f)+val13);
        data0[alu3+306] = ((acc45*0.125f)+val13);
        data0[alu3+562] = ((acc46*0.125f)+val13);
        data0[alu3+818] = ((acc47*0.125f)+val13);
        data0[alu3+3] = ((acc48*0.125f)+val2);
        data0[alu3+259] = ((acc49*0.125f)+val2);
        data0[alu3+515] = ((acc50*0.125f)+val2);
        data0[alu3+771] = ((acc51*0.125f)+val2);
        data0[alu3+19] = ((acc52*0.125f)+val6);
        data0[alu3+275] = ((acc53*0.125f)+val6);
        data0[alu3+531] = ((acc54*0.125f)+val6);
        data0[alu3+787] = ((acc55*0.125f)+val6);
        data0[alu3+35] = ((acc56*0.125f)+val10);
        data0[alu3+291] = ((acc57*0.125f)+val10);
        data0[alu3+547] = ((acc58*0.125f)+val10);
        data0[alu3+803] = ((acc59*0.125f)+val10);
        data0[alu3+51] = ((acc60*0.125f)+val14);
        data0[alu3+307] = ((acc61*0.125f)+val14);
        data0[alu3+563] = ((acc62*0.125f)+val14);
        data0[alu3+819] = ((acc63*0.125f)+val14);
      }
    }
  }
}
"""

entry = """unsigned long long HAP_perf_get_time_us(void);
int entry(unsigned long long handle, unsigned int sc, void* pra) {
return HAP_perf_get_time_us() == 1 ? 4 : 0;
}
"""

if __name__ == "__main__":
  dev = DSPDevice()

  bufs = [dev.allocator.alloc(0x60000) for _ in range(4)]

  only_entry = dev.compiler.compile(entry)
  app1 = dev.runtime("test", only_entry)
  x = app1(*bufs)

  entry_n_unsued_code = dev.compiler.compile(kernel + "\n" + entry)
  app2 = dev.runtime("test", entry_n_unsued_code)
  x = app2(*bufs)
