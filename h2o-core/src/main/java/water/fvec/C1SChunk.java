package water.fvec;

import water.util.PrettyPrint;
import water.util.UnsafeUtils;

/**
 * The scale/bias function, where data is in SIGNED bytes before scaling.
 */
public final class C1SChunk extends CSChunk {
  C1SChunk( byte[] bs, long bias, int scale ) { super(bs,bias,scale,0);}

  @Override protected final double atd_impl( int i ) {
    return getD(0xFF&_mem[_OFF+i],C1Chunk._NA);
  }
  @Override protected final boolean isNA_impl( int i ) { return (0xFF&_mem[i+_OFF]) == C1Chunk._NA; }
  @Override boolean setNA_impl(int idx) { _mem[idx+_OFF] = (byte)C1Chunk._NA; return true; }



  @Override
  protected boolean set_impl(int i, double x) {
    if(Double.isNaN(x)) return setNA_impl(i);
    int y = getScaledValue(x, C1Chunk._NA);
    if(y == C1Chunk._NA) return false;
    byte b = (byte)y;
    if(b != y) return false;
    _mem[_OFF+i] = b;
    return true;
  }

  /**
   * Dense bulk interface, fetch values from the given range
   * @param vals
   * @param from
   * @param to
   */
  @Override
  public double [] getDoubles(double [] vals, int from, int to, double NA){
    for(int i = from; i < to; ++i)
      vals[i-from] = getD(0xFF&_mem[_OFF+i],C1Chunk._NA);
    return vals;
  }
  /**
   * Dense bulk interface, fetch values from the given ids
   * @param vals
   * @param ids
   */
  @Override
  public double [] getDoubles(double [] vals, int [] ids){
    int j = 0;
    for(int i:ids)
      vals[j++] = getD(0xFF&_mem[_OFF+i],C1Chunk._NA);
    return vals;
  }

  private <T extends ChunkVisitor> void processRow(T v, int i, long bias, int exp){
    long x = 0xFF & _mem[_OFF + i];
    if(x == C1Chunk._NA) v.addNAs(1);
    else v.addValue(x + bias, exp);
  }

  @Override
  protected <T extends ChunkVisitor> T processRows2(T v, int from, int to, long bias, int exp) {
    for(int i = from; i < to; ++i)
      processRow(v,i,bias,exp);
    return v;
  }

  @Override
  protected <T extends ChunkVisitor> T processRows2(T v, int from, int to) {
    for(int i = from; i < to; ++i)
      v.addValue(getD(0xFF&_mem[_OFF+i],C1Chunk._NA));
    return v;
  }

  @Override
  protected <T extends ChunkVisitor> T processRows2(T v, int [] ids, long bias, int exp) {
    for(int i:ids)
      processRow(v,i,bias,exp);
    return v;
  }

  @Override
  protected <T extends ChunkVisitor> T processRows2(T v, int [] ids) {
    for(int i:ids)
      v.addValue(getD(0xFF&_mem[_OFF+i],C1Chunk._NA));
    return v;
  }


}
