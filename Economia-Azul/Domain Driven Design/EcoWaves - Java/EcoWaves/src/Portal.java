import java.util.Date;

public class Portal {
    private int id_post;
    private String titulo;
    private String conteudo;
    private Date data_publicacao;


    public void adicionarPost(){}
    public void editarPost(){}
    public void visualizarPosts(){}

//  encapsulamento

    public int getId_post() {
        return id_post;
    }

    public void setId_post(int id_post) {
        this.id_post = id_post;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getConteudo() {
        return conteudo;
    }

    public void setConteudo(String conteudo) {
        this.conteudo = conteudo;
    }

    public Date getData_publicacao() {
        return data_publicacao;
    }

    public void setData_publicacao(Date data_publicacao) {
        this.data_publicacao = data_publicacao;
    }
}
