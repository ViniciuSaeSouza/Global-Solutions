public class ChatBot {
    private int id_chat = 0;
    private String nome;
    private String tipo;


    public ChatBot(String nome, String tipo){
        this.id_chat = id_chat+1;
        this.nome = nome;
        this.tipo = tipo;
    }

//    uma simulação
    public String responderPerguntas(String pergunta){
        switch (pergunta){
            case "O que é ecoturismo?":
                return "Ecoturismo é uma forma de turismo voltado para a apreciação de ambientes naturais.";
            case "Como posso me inscrever em uma atividade?":
                return "Para se inscrever em uma atividade, você deve estar logado e acessar a página da atividade desejada.";
            default:
                return "Desculpe, não entendi a pergunta.";
        }
    }

    //com a API será adicionado ao java para dar suporte
    public void fornecerSuporte(){}

//  encapsulamento

    public int getId_chat() {
        return id_chat;
    }

    public void setId_chat(int id_chat) {
        this.id_chat = id_chat;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
}
