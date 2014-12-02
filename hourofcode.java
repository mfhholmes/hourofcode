public class hourofcode {
  public static void main(String[] args){
    //java has no standard library for command-line arguments!
    //hacking together nastiness by ignoring any argument that starts with a dash
    String name = "";
    for (String s: args){
      String dash = s.substring(0,1);
      if(dash!="-"){
        name = s;
      }
    }
    System.out.println("hello "+name);
  }
}
