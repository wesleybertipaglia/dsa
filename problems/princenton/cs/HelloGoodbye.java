public class HelloGoodbye {
    public static void main(String[] args) {
        if (args.length == 0) {
            args[0] = "World";
            args[1] = "World";
        }

        String hello = String.format("Hello %s and %s.", args[0], args[1]);
        System.out.println(hello);

        String bye = String.format("Goodbye %s and %s.", args[0], args[1]);
        System.out.println(bye);
    }
}
