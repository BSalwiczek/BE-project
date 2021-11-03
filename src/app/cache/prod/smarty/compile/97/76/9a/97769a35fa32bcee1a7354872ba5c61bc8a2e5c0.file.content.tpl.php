<?php /* Smarty version Smarty-3.1.19, created on 2021-11-03 13:45:01
         compiled from "/var/www/html/admin1/themes/default/template/content.tpl" */ ?>
<?php /*%%SmartyHeaderCode:21002820666182844d922182-04631341%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '97769a35fa32bcee1a7354872ba5c61bc8a2e5c0' => 
    array (
      0 => '/var/www/html/admin1/themes/default/template/content.tpl',
      1 => 1490891120,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '21002820666182844d922182-04631341',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'content' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.19',
  'unifunc' => 'content_6182844d9268b3_08256337',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_6182844d9268b3_08256337')) {function content_6182844d9268b3_08256337($_smarty_tpl) {?>
<div id="ajax_confirmation" class="alert alert-success hide"></div>

<div id="ajaxBox" style="display:none"></div>


<div class="row">
	<div class="col-lg-12">
		<?php if (isset($_smarty_tpl->tpl_vars['content']->value)) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }} ?>
