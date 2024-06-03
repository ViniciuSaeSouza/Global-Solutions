import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class ONG extends Pessoa{
    private String descricao;
    private List<Atividades> atividades;

    public ONG(int id_ong, String razao_social, String email, String senha, String descricao){
        super(id_ong, razao_social, email, senha );
        this.descricao = descricao;
        this.atividades = new ArrayList<>();
    }
    public void adicionarAtividade(Atividades atividade){
        this.atividades.add(atividade);
    }
    public void editarAtividade(int atividadeId, String novo_nome, String nova_descricao, Date nova_data, String nova_hora, String novo_local, int novas_vagas){
        for(Atividades atividade : this.atividades){
            if(atividade.getId_atividade() == atividadeId){
                atividade.setNome_atividade(novo_nome);
                atividade.setDescricao_atividade(nova_descricao);
                atividade.setData(nova_data);
                atividade.setHora(nova_hora);
                atividade.setLocal(novo_local);
                atividade.setVagas(novas_vagas);
            }
        }
    }
    public void visualizarInscritos(){}

//    encapsulamento

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public List<Atividades> getAtividades() {
        return atividades;
    }

    public void setAtividades(List<Atividades> atividades) {
        this.atividades = atividades;
    }
}
