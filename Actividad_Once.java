import java.util.Random;

public class Actividad_Once {

	public static void main(String[] args) {
		
		Random a = new Random();
		int x;
		int b = a.nextInt (20 - 1) +1;
		
		for(int i =1; i<b; i++){
			
			x = a.nextInt(65 - 18) + 18;
			
		    System.out.println("numero aleatorio : " + x);
		}
		
	}

}
