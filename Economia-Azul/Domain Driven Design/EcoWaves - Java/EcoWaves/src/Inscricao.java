import java.util.Date;

public class Inscricao {
    private int id_inscricao;
    private Date data_inscricao;

    private Voluntario voluntario;
    private Atividades atividades;

    public Inscricao(int id, Date data_inscricao,Voluntario voluntario, Atividades atividade){
        this.id_inscricao = id;
        this.voluntario = voluntario;
        this.atividades = atividade;
        this.data_inscricao = data_inscricao;
    }

//  encapsulamento

    public int getId_inscricao() {
        return id_inscricao;
    }

    public void setId_inscricao(int id_inscricao) {
        this.id_inscricao = id_inscricao;
    }

    public Date getData_inscricao() {
        return data_inscricao;
    }

    public void setData_inscricao(Date data_inscricao) {
        this.data_inscricao = data_inscricao;
    }

    public Voluntario getVoluntario() {
        return voluntario;
    }

    public void setVoluntario(Voluntario voluntario) {
        this.voluntario = voluntario;
    }

    public Atividades getAtividades() {
        return atividades;
    }

    public void setAtividades(Atividades atividades) {
        this.atividades = atividades;
    }
}
