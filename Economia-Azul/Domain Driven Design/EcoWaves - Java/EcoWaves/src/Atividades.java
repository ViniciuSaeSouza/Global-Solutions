import java.util.Date;

public class Atividades {
    private int id_atividade;
    private String nome_atividade;
    private String descricao_atividade;
    private Date data;
    private String hora;
    private String local;
    private int vagas;
    private String tipo;

    public  Atividades(int id, String nome_atividade, String descricao_atividade, Date data,String hora,String local, int vagas, String tipo){
        this.id_atividade = id;
        this.nome_atividade = nome_atividade;
        this.descricao_atividade = descricao_atividade;
        this.data = data;
        this.hora = hora;
        this.local = local;
        this.vagas = vagas;
    }

//  encapsulamento

    public int getId_atividade() {
        return id_atividade;
    }

    public void setId_atividade(int id_atividade) {
        this.id_atividade = id_atividade;
    }

    public String getNome_atividade() {
        return nome_atividade;
    }

    public void setNome_atividade(String nome_atividade) {
        this.nome_atividade = nome_atividade;
    }

    public String getDescricao_atividade() {
        return descricao_atividade;
    }

    public void setDescricao_atividade(String descricao_atividade) {
        this.descricao_atividade = descricao_atividade;
    }

    public Date getData() {
        return data;
    }

    public void setData(Date data) {
        this.data = data;
    }

    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }

    public String getLocal() {
        return local;
    }

    public void setLocal(String local) {
        this.local = local;
    }

    public int getVagas() {
        return vagas;
    }

    public void setVagas(int vagas) {
        this.vagas = vagas;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
}
