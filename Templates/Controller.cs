using Acc.Comum;
using Acc.Comum.Model;
using Microsoft.Practices.Unity;
using SIFSE.Model.Constantes;
using SIFSE.Web.Common;
using System.Web.Mvc;

namespace SIFSE.Web.Areas.$area$.Controllers
{
    public class $controller$Controller : BaseController
    {
        #region Dependencies
        //[Dependency]
        //public Service Service { get; set; }
        #endregion Dependencies

        #region TemplateActions
        [SessionExpire]
        [EncryptedActionParameter]
        public virtual ActionResult $action$([Bind(Prefix = "LineID")] string ID, [Bind(Prefix = "Modo")] string Modo)
        {
            TipoModoAcesso modoAcesso =  getTipoModoAcesso(Modo);
            if (!LockEControloDeAcesso(ID, modoAcesso, (int)Menu.))
            {
                return RedirectToAction(NeosMVC.Comum.Comum.ActionNames.MensagemControloAcesso, NeosMVC.Comum.Comum.Name, new { Area = "Comum" });
            }

            return View();
        }

        [SessionExpire]
        [HttpPost]
        public virtual ActionResult $action$(BaseEntity model)
        {
            if (!LockEControloDeAcesso(model.ID, model.Modo, (int)Menu.))
            {
                return RedirectToAction(NeosMVC.Comum.Comum.ActionNames.MensagemControloAcesso, NeosMVC.Comum.Comum.Name, new { Area = "Comum" });
            }
        }
        #endregion TemplateActions
    }
}