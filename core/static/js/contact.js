$(document).ready(function(){
    (function($) {
        "use strict";

        jQuery.validator.addMethod('answercheck', function (value, element) {
            return this.optional(element) || /^\bcat\b$/.test(value)
        }, "type the correct answer -_-");

        // validate contactForm form
        $(function() {
            $('#contactForm').validate({
                rules: {
                    name: { required: true },
                    subject: { required: true },
                    email: { required: true, email: true },
                    message: { required: true }
                },
                messages: {
                    name: { required: "Por favor, insira seu nome" },
                    subject: { required: "Por favor, insira o assunto" },
                    email: { required: "Por favor, insira seu email" },
                    message: { required: "Por favor, escreva uma mensagem" }
                },

                // Classe que será aplicada aos elementos com erro
                errorClass: "text-danger",  // bootstrap já tem essa classe para vermelho

                // Quando um campo estiver com erro
                highlight: function(element, errorClass, validClass) {
                    $(element).addClass(errorClass).removeClass(validClass);
                },

                // Quando o erro for corrigido
                unhighlight: function(element, errorClass, validClass) {
                    $(element).removeClass(errorClass).addClass(validClass);
                },

                submitHandler: function(form) {
                    $(form).ajaxSubmit({
                        type: "POST",
                        data: $(form).serialize(),
                        url: "contact_process.php",
                        success: function() {
                            $('#contactForm :input').attr('disabled', 'disabled');
                            $('#contactForm').fadeTo("slow", 1, function() {
                                $(this).find(':input').attr('disabled', 'disabled');
                                $(this).find('label').css('cursor','default');
                                $('#success').fadeIn()
                                $('.modal').modal('hide');
                                $('#success').modal('show');
                            });
                        },
                        error: function() {
                            $('#contactForm').fadeTo("slow", 1, function() {
                                $('#error').fadeIn()
                                $('.modal').modal('hide');
                                $('#error').modal('show');
                            });
                        }
                    });
                }
            });
        });
    })(jQuery);
});
