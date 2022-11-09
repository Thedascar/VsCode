using System; // Importações

namespace MeuApp // Namespaces
{
    class Program // Classe
    {
        static void Main(string[] args) // Método main principal
        {
           // Declaração de Váriaveis
           // int idade; // correto começa com zero
           // int idade = 25; // correta começa com 25
           // var idade 25; // correto inica com 25
           // var idade; // errado var precisa ser iniciado
           // Console.WriteLine(idade);

           //------------------------------------------------------
           // Constante as constantes não podem ser alteradas
           // const int IDADE_MINIMA; // correto começa com zero
           // const int IDADE_MINIMA = 25; // correta começa com 25
           // const var IDADE_MINIMA = 25; // Errado var nao recebe const
           // const var IDADE_MINIMA; // erradovar não recebe const
           // Console.WriteLine(idade);
           
           //-------------------------------------------------------
           // Tipos Primitivos.. em dotNet
           // Tipos built-in types
           
           // ----- Tipos Byte --------//
           // Temos os bytes e sbytes pode ser signed(-) e unsined
           // byte meuByte =  127;
           // Console.WriteLine(meuByte);
           
           // ----- Tipos Inteiros --------//
           // short/ushort
           // int/uint
           // long/ulong
           // int meuInt =  127;
           // Console.WriteLine(meuInt);
            
           // ----- Tipos Reais --------//
           // float (Notação F)
           // double
           // decimal (Notação M)
           // var salario = 2.500;
           // float salario2 = 2.500f; // Com notação
           // decimal salario3 = 2.500m; // Com notação
           // Console.WriteLine(salario);
           
           // ----- Tipos Booleano --------//
           // true or false
           // bool usuarioJaCadastrado = false;
           // Console.WriteLine(usuarioJaCadastrado);

           // ----- Tipos Char --------//
           // armazena apenas um caracter   
           // usa formato Unicode
           // usa aspas simples (' ')
           // char primeiraLetra ='M';
           // Console.WriteLine(primeiraLetra);

           // ----- Tipos String --------//
           // armazena uma cadeia de caracteres
           // usa aspas duplas (" ")
           // string primeiraLetra = "C";
           // string text = "Meu Texto";
           // Console.WriteLine(primeiraLetra);

            // ----- Tipos String --------//
            // substitui o nome do tipo
            // var idade = 25; // int
            // var idade2 = "Lucas";// string
            // var numero = 1.5; // double
            // Console.WriteLine(idade2);

            // ----- Tipos String --------//
            // tipo objeto
            // tipo generico
            // object idade = 25; // será do tipo object
            // object nome = "Lucas"; // será do tipo object
            // Console.WriteLine(nome);

             // ----- Tipos Nullabel Types --------//
             // significa vazio
             // sempre usa (?) na frent do tipo
             // int? idade = null;
             // Console.WriteLine(idade);

             // ----- Alias --------//
             // apelido que todo tipo tem
             // System.String tem o alias (string)

             // ----- Valores Padrões --------//
             // numca vem nulo 
             // sempre inicia com valor
             // int => 0
             // float => 0
             // decimal => 0
             // bool => false
             // char => '\0'
             // String => ""

             // ----- Conversão implicita --------//
             // converter o tipo da variável
             // float valor = 25.8f;
             // int outro 25;
             // valor = outro; // conversão implícita

             // ----- Conversão implicita --------/
             // ocorre quando os tipo não são compatíveis
             // int inteiro = 100;
             //uint inteiroSemSinal = (uint)inteiro;// Conversão explícita
   
            // ----- Parse --------//
            // todos os métodos presentes em todo tipo primitivo
            // usado para converter um caractere ou string para um tipo
            //int inteiro = 100;
            //float real = 25.5f;
             
            //inteiro = real; // não pode ocorre um erro inteira nao vira real
            //real = inteiro; // pode 100.0f
            
            // precisamos converter a var real para .ToStrinf()....
            // para pdoe executar o Parse
            // Parse so converte String
            //inteiro = int.Parse(real.ToString());// ocorre erro

            //Console.WriteLine(inteiro);


            // ----- Convert--------//
            // permite voncerter vários tipos de valor
            // não apenas string
            // devemos informar o tipo na chamada de conversão
            
            // int inteiro = Convert.ToInt32("100");
            // int inteiro = 100;
            // float real = 25.5f;
            
            // inteiro = real; // não pode ocorre um erro inteira nao vira real
            // real = inteiro; // pode 100.0f

            // inteiro = (int)real;// COnversão forçada

           // inteiro = Convert.ToInt32(real); // conversão usando converte
           

        }
    }
}
