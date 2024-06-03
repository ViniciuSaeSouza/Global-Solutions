public class Parceiro extends Pessoa{
    private int desconto;
    private String cupom;

    public Parceiro(int id_parceiro, String razao_social, String email, String senha, int desconto, String cupom){
        super(id_parceiro, razao_social, email, senha );
        this.desconto = desconto;
        this.cupom = cupom;
    }
    public void editarDesconto(int novo_desconto, String novo_cupom){
        this.cupom = novo_cupom;
        this.desconto = novo_desconto;
    }
    public void adicionarDesconto(int desconto, String cupom){
        this.desconto = desconto;
        this.cupom = cupom;
    }
}
