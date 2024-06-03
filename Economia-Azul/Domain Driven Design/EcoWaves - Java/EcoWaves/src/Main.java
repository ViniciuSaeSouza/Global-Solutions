import java.util.Date;

public class Main {
    public static void main(String[] args) {
        // Registro de uma ONG
        ONG ong1 = new ONG(1, "ONG Oceano Limpo", "contato@oceano.org", "ong123", "Proteção dos oceanos");

        // Registro de um usuário
        Voluntario usuario1 = new Voluntario(1, "João Silva", "joao@gmail.com", "usuario123", "comum");

        // ONG adiciona uma atividade
        Atividades atividade1 = new Atividades(1, "Limpeza de Praia", "Evento para limpar a praia do Leme", new Date(2024, 6, 15), "09:00", "Praia do Leme", 50, "ecovoluntariado");
        ong1.adicionarAtividade(atividade1);

        // Usuário se inscreve na atividade
        Inscricao inscricao1 = new Inscricao(1, new Date(2024, 05, 10), usuario1, atividade1);

        // Função de simulação de inscrição e mandava pro banco de dados
        registrarInscricao(inscricao1, atividade1);

        // Visualizando as atividades da ONG
        for (Atividades atividade : ong1.getAtividades()) {
            System.out.println("Atividade: " + atividade.getNome_atividade() + ", Descrição: " + atividade.getDescricao_atividade() + ", Data: " + atividade.getData() + ", Vagas: " + atividade.getVagas());
        }

        // Editando atividade
        ong1.editarAtividade(1, "Limpeza de Praia - Atualizado", "Evento para limpar a praia do Leme", new Date(2024, 6, 15), "09:00", "Praia do Leme", 100);

        // Visualizando as atividades da ONG após a edição
        for (Atividades atividade : ong1.getAtividades()) {
            System.out.println("Atividade: " + atividade.getNome_atividade() + ", Descrição: " + atividade.getDescricao_atividade() + ", Data: " + atividade.getData() + ", Vagas: " + atividade.getVagas());
        }

        // Exemplo de uso do Chatbot
        ChatBot chatBot = new ChatBot("EcoBot","Suporte");

        String pergunta1 = "O que é ecoturismo?";
        String resposta1 = chatBot.responderPerguntas(pergunta1);
        System.out.println("Chatbot: " + resposta1);

        String pergunta2 = "Como posso me inscrever em uma atividade?";
        String resposta2 = chatBot.responderPerguntas(pergunta2);
        System.out.println("Chatbot: " + resposta2);
    }

    public static void registrarInscricao(Inscricao inscricao, Atividades atividade) {
        if (atividade.getVagas() > 0) {
            atividade.setVagas(atividade.getVagas() - 1);

            System.out.println("Voluntario: " + inscricao.getVoluntario().nome + " inscrito na atividade " + inscricao.getAtividades().getNome_atividade()+ ". Vagas restantes: " + atividade.getVagas());
        } else {
            System.out.println("Não há vagas disponíveis para esta atividade.");
        }
    }
}
